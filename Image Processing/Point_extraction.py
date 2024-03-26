import cv2
import numpy as np
from scipy import ndimage

#----------------------------------------Canny edge detction ------------------
img = cv2.imread("Image Processing/im1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Threshold Values
t_lower = 150  # Lower Threshold 
t_upper = 300  # Upper threshold
edges = cv2.Canny(gray, t_lower, t_upper) 

# cv2.imshow('edge', edges) 
# cv2.waitKey(0) 
# cv2.destroyAllWindows() 
#----------------------------------------Hough Tranforms ----------------------

lines_list =[]
lines = cv2.HoughLinesP(
            edges, # Input edge image
            1, # Distance resolution in pixels
            np.pi/180, # Angle resolution in radians
            threshold=200, # Min number of votes for valid line
            minLineLength=280, # Min allowed length of line
            maxLineGap=25 # Max allowed gap between line for joining them
            )

# Iterate over points
infinity = float('inf')
negative_infinity = float('-inf')
for points in lines:
      # Extracted points nested in the list
    x1,y1,x2,y2=points[0]
    length = y2-y1
    x_length = x2-x1
    if length<0 :
        length = length *-1
    if length >=50:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
        lines_list.append([(x1,y1),(x2,y2)])
        print(points)
       
    # Draw the lines joing the points
    # On the original image
    #cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    # Maintain a simples lookup list for points
    #lines_list.append([(x1,y1),(x2,y2)])
    
# Show the result image
# cv2.imshow('Image with Key Points', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# #----------------------------------------Rotation ------------------------------
# # Compute the angle of the lines
# angles = [np.arctan2(y2 - y1, x2 - x1) for (x1, y1), (x2, y2) in lines_list]
# # Compute the mean angle and rotate the image to get vertical lines
# mean_angle = np.mean(angles)
# rotated_image = ndimage.rotate(img, np.degrees(mean_angle), reshape=False)

# cv2.imshow('Rotated_image', rotated_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#----------------------------------------Hough Transform for Ellipses ------------------------------
# Convert the rotated image to grayscale and apply Canny edge detection
gray_rotated = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges_rotated = cv2.Canny(gray_rotated, t_lower, t_upper)

# Apply Hough transform for ellipses
ellipses = cv2.HoughCircles(edges_rotated, cv2.HOUGH_GRADIENT, 1, 20,
                            param1=300,
                            param2=25,
                            minRadius=0,
                            maxRadius=40)

# Select the ellipses of interest and extract the key points
key_points = []
if ellipses is not None:
    ellipses = np.uint16(np.around(ellipses))
    for i in ellipses[0,:]:
        # Draw the outer circle
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # Draw the center of the circle
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
        # Add the center of the ellipse to the key points
        key_points.append((i[0], i[1]))

# Show the result image
cv2.imshow('Image with Key Points', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
