import cv2
import numpy as np

#-------------------Canny edge detction ------------------
img = cv2.imread("Image Processing/im1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Threshold Values
t_lower = 50  # Lower Threshold 
t_upper = 150  # Upper threshold
edges = cv2.Canny(gray, t_lower, t_upper) 

#cv2.imshow('edge', edges) 
#cv2.waitKey(0) 
#cv2.destroyAllWindows() 
#------------------Hough Tranform Vertical ----------------------

lines_list =[]
lines = cv2.HoughLinesP(
            edges, # Input edge image
            1, # Distance resolution in pixels
            np.pi/180, # Angle resolution in radians
            threshold=100, # Min number of votes for valid line
            minLineLength=5, # Min allowed length of line
            maxLineGap=10 # Max allowed gap between line for joining them
            )


# Iterate over points
infinity = float('inf')
negative_infinity = float('-inf')
for points in lines:
      # Extracted points nested in the list
    x1,y1,x2,y2=points[0]
    slope = (y2-y1)/(x2-x1)
    length = y2-y1
    if length < 0:
        length = length*-1
    if slope == infinity or slope == negative_infinity:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
        lines_list.append([(x1,y1),(x2,y2)])
        print(length)

    # Draw the lines joing the points
    # On the original image
    #cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    # Maintain a simples lookup list for points
    #lines_list.append([(x1,y1),(x2,y2)])
    
# Save the result image
cv2.imshow('Image with Key Points', img)
cv2.waitKey(0)
cv2.destroyAllWindows()