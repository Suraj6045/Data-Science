import cv2
import numpy as np

sih_image = cv2.imread("OpenCv\ImageManipulation\image.png")

cropped = sih_image[100:300 , 0 :150]

cv2.imshow("Image" , cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imwrite("OpenCv\BlackAndWhite\image2.png" , blackAndWhite)