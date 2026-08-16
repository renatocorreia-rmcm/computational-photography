import cv2 as cv
import numpy as np
from skimage import data
from matplotlib import pyplot




img = data.moon()

pyplot.hist(img.ravel(), alpha=0.5)


N = img.ravel().shape[0]
print(N)

cumulated_count = np.zeros(shape=(256), dtype=np.int32)

for rk in img.ravel():
    cumulated_count[rk]+=1

for i in range(1, len(cumulated_count)):
    cumulated_count[i]+=cumulated_count[i-1]


for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img[i,j] = np.round((255*cumulated_count[img[i,j]])/N)

pyplot.hist(img.ravel(), alpha=0.5)

pyplot.plot(range(256), cumulated_count)


cv.imshow("original", data.moon())
cv.imshow("processado", img)
pyplot.show()


cv.waitKey(0)
cv.destroyAllWindows()