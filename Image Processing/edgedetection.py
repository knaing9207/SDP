import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('pillimage.jpg')

blur = cv2.GaussianBlur(img,(5,5),0)

gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 200, 5)

cv2.imwrite("edges.jpg", edges)