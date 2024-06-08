# Write your code here :-)
import numpy as np
import cv2

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
image= cv2.imread('input-image.jpg')

y, x, _= image.shape
data= np.reshape(image, (x*y,3))
data= np.float32(data)

n= 7
criteria= (cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER, 10, 3.0)
flags= cv2.KMEANS_RANDOM_CENTERS

_, _, centers= cv2.kmeans(data, n, None, criteria, 10, flags)

def create_box(x,y,color):
    bar= np.zeros((y,x,3), np.uint8)
    bar[:]= color
    r, g, b= int(color[2]), int(color[1]), int(color[0])

    return bar, (r, g, b)


bars= []
rgb_values= []

for row in centers:
    bar, rgb= create_box(100, 100, row)
    bars.append(bar)
    rgb_values.append(rgb)

palette= np.hstack(bars)

cv2.imshow('Palette', palette)

cv2.imshow('image', image)
cv2.waitKey(0)

