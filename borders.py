import cv2 as cv
import numpy as np


def show(img):
    cv.imshow("", img); cv.waitKey(0)


img = cv.imread("assets/smallpuppy.png")

show(img)

show(
    cv.copyMakeBorder(img,100,100,100,100,cv.BORDER_REPLICATE)
)

show(
    cv.copyMakeBorder(img,100,100,100,100,cv.BORDER_REFLECT)
)

show(
    cv.copyMakeBorder(img,1000,1000,1000,1000,cv.BORDER_REFLECT_101)
)

show(
    cv.copyMakeBorder(img,100,100,100,100,cv.BORDER_WRAP)
)

show(
    cv.copyMakeBorder(img,100,100,100,100,cv.BORDER_CONSTANT,value=[255,255,0])
)
