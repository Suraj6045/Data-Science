import cv2
import numpy as np

sih_image = cv2.imread("OpenCv\ImageManipulation\image.png")

resized = cv2.resize(sih_image , (300 , 300))

cv2.imshow("Image" , resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imwrite("OpenCv\BlackAndWhite\image2.png" , blackAndWhite)