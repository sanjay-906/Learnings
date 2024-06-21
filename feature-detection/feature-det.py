# Write your code here :-)
import os
import matplotlib.pyplot as plt
import numpy as np
import cv2


def SIFT():
    imggrey= cv2.imread("watermelon.jpg", cv2.IMREAD_GRAYSCALE)
    hessian_threshold= 5000
    sift= cv2.SIFT_create(hessian_threshold)
    keypoints= sift.detect(imggrey, None)
    imggrey= cv2.drawKeypoints(imggrey, keypoints, imggrey, flags= cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    plt.figure()
    plt.imshow(imggrey)
    plt.show()

def ORB():
    imggrey= cv2.imread("watermelon.jpg", cv2.IMREAD_GRAYSCALE)
    orb= cv2.ORB_create()
    keypoints= orb.detect(imggrey, None)
    keypoints, _= orb.compute(imggrey, keypoints)
    imggrey= cv2.drawKeypoints(imggrey, keypoints, imggrey, flags= cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    plt.figure()
    plt.imshow(imggrey)
    plt.show()

def good_corner_detection():
    imggrey= cv2.imread("watermelon.jpg", cv2.IMREAD_GRAYSCALE)
    imgrgb= cv2.imread("watermelon.jpg")
    imgrgb= cv2.cvtColor(imgrgb, cv2.COLOR_BGR2RGB)
    max_corners= 100
    quality= 0.01
    min_distance= 20

    corners= cv2.goodFeaturesToTrack(imggrey, max_corners, quality, min_distance)
    for corner in corners:
        x= int(corner[0][0])
        y= int(corner[0][1])
        cv2.circle(imgrgb, (x,y), 10, (255,0,0), -1)

    plt.figure()
    plt.imshow(imgrgb)
    plt.show()
if __name__== "__main__":
    SIFT()
    ORB()
    good_corner_detection()
