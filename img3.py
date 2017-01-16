import numpy as np
import cv2
import matplotlib.pyplot as plt
img =cv2.imread('watch.jpg',2)
"""cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindow()"""
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.show()