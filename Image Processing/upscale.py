import cv2
import matplotlib.pyplot as plt

sr = cv2.dnn_superres.DnnSuperResImpl_create()
 
img = cv2.imread('drug1.jpg', cv2.IMREAD_UNCHANGED)

path = "LapSRN_x8.pb"
 
sr.readModel(path)
 
sr.setModel("lapsrn",8)
 
result = sr.upsample(img)
 
# Resized image
resized = cv2.resize(img,dsize=None,fx=4,fy=4)
 
plt.figure(figsize=(12,8))
plt.subplot(1,3,1)
# Original image
plt.imshow(img[:,:,::-1])
plt.subplot(1,3,2)
# SR upscaled
plt.imshow(result[:,:,::-1])
plt.subplot(1,3,3)
cv2.imwrite("srupscaled.png", result)
# OpenCV upscaled
plt.imshow(resized[:,:,::-1])
plt.show()
cv2.imwrite("cvupscaled.png", resized)