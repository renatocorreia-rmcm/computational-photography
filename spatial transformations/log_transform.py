import cv2 as cv
import numpy as np
import math

img = cv.imread("assets/smallpuppy.png", cv.IMREAD_GRAYSCALE)

def log_transform_loop(img):
    height, width = img.shape
    newimg = np.zeros(shape=img.shape, dtype=np.uint8)
    

    c = 255 / math.log(1 + 255)

    for i in range(height):       # Iterate over rows
        for j in range(width):    # Iterate over columns
            r = img[i, j]
            newimg[i, j] = int(c * math.log(1 + r))
            
    return newimg

cv.imshow("Original", img)
cv.imshow("Log Transformed", log_transform_loop(img))
cv.waitKey(0)
cv.destroyAllWindows()