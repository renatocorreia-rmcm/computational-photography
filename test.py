import cv2 as cv
import numpy as np


def show(img):
    cv.imshow("", img); cv.waitKey(0)


img = cv.imread("assets/puppy.png")

img = cv.resize(src=img, dsize=None, fx=1/3, fy=1/3)
