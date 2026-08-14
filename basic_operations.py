import cv2 as cv
import numpy as np


def show(img):
    cv.imshow("", img); cv.waitKey(0)


img = cv.imread("assets/smallpuppy.png")

show(img)



roi = img[20:100, 50:70]  # region of interest

show(roi)

b, g, r = cv.split(img)  # same as b, g, r = img[:, :]
show(b)
show(g)
show(r)

img = cv.merge((g,r,b))  # shuffling channels
show(img)


