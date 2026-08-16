import cv2 as cv
import numpy as np
from skimage import data


def gammacorrect(img, gamma):
    height, width = img.shape
    newimg = np.zeros(shape=img.shape, dtype=np.uint8)

    for i in range(height):       # Iterate over rows
        for j in range(width):    # Iterate over columns
            newimg[i, j] = int(255 * (img[i,j]/255)**gamma)
            
    return newimg

for i in range(1, 13):
    cv.imshow(f"{i/4}", gammacorrect(data.moon(), i/4))

cv.waitKey(0)
cv.destroyAllWindows()