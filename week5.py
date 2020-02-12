import os
import cv2
import numpy as np
img = cv2.imread("container.jpg",cv2.IMREAD_COLOR)
rcw_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Result" ,rcw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()