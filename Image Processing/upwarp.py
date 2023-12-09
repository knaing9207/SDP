import cv2
import numpy as np

# Load the image of the cylindrical shape.
img = cv2.imread('drug1.jpg')

# Convert the image to grayscale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply the dewarping algorithm to the image.
warped = cv2.warpAffine(gray, M, (img.shape[1], img.shape[0]))

# Save the dewarped image.
cv2.imwrite('dewarped_image.png', warped)