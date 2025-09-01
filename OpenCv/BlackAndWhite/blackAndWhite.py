import cv2
import numpy as np

sih_image = cv2.imread("OpenCv\BlackAndWhite\image.png")

blackAndWhite = cv2.cvtColor(sih_image , cv2.COLOR_BGR2GRAY)

cv2.imshow("Image" , blackAndWhite)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("OpenCv\BlackAndWhite\image2.png" , blackAndWhite)