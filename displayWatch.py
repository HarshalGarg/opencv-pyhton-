import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('watch.jpg',0)
"""cv2.imshow('watch pic',img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""
plt.imshow(img,cmap='gray')
plt.show()