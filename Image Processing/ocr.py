import pytesseract
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image
image = cv2.imread('stitched_image.jpg')

norm_img = np.zeros((image.shape[0], image.shape[1]))
img = cv2.normalize(image, norm_img, 0, 255, cv2.NORM_MINMAX)

# Create the sharpening kernel 
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) 

# Sharpen the image 
sharpened_image = cv2.filter2D(img, -1, kernel) 

denoised = cv2.fastNlMeansDenoising(sharpened_image, None, 20, 7, 21) 

# Convert the image to grayscale
grayscale_image = cv2.cvtColor(denoised, cv2.COLOR_BGR2GRAY)

binary_image = cv2.threshold(grayscale_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# # Perform OCR using PyTesseract
# text = pytesseract.image_to_string(binary_image)

# # Print the extracted text
# print(text)

# cv2.imwrite('binary_image.png', binary_image)

# Crop the image
name = binary_image[103:182, 434:750]

# Run the OCR on the cropped image
text = pytesseract.image_to_string(name)

print(text)

# Crop the image
quantity = binary_image[182:203, 19:83]

# Get the width and height of the image
width = quantity.shape[1]
height = quantity.shape[0]

# Calculate the new width and height
new_width = int(width * 3/4)
new_height = int(height * 3/4)

# Resize the image
quantity_resized = cv2.resize(quantity, (new_width, new_height))

# Run the OCR on the cropped image
text2 = pytesseract.image_to_string(quantity_resized)

cv2.imwrite('cropped.png', quantity_resized)
cv2.imwrite('cropped2.png', name)

# Extract the text from the OCR output
print(text2)