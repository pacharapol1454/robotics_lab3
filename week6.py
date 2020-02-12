import os
import cv2
import numpy as np
img = cv2.imread("container.jpg",cv2.IMREAD_COLOR)
crop = img[85:310, 330:450]
cv2.imshow("Result" ,crop)
cv2.waitKey(0)
cv2.destroyAllWindows()