import cv2 as cv
import numpy as np

img = cv.imread("assets/puppy.png")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

c = float(input("c: "))
gamma = float(input("gamma: "))

img = np.int8(c*np.power(img, gamma))

cv.imshow("", img); cv.waitKey(0)
