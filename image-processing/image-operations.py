import numpy as np
import cv2
import matplotlib.pyplot as plt

x= 1
img= cv2.imread("demo.jpg",x)
'''
x= 1 or cv2.IMREAD_COLOR, reads the image as in color, no transperency
x= 0 or cv2.IMREAD_GRAYSCALE, reads image in b/w
x= -1 or cv2.IMREAD_UNCHANGED, as it is, including alpha channel(transperency)
'''

'''Display image'''
#cv2.imshow("image",img)
#cv2.waitKey(0)

#plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#plt.show()

'''
Display only the channels
'''
blue_img= img[:,:,0]
green_img= img[:,:,1]
red_img= img[:,:,2]

temp= np.zeros(img.shape, np.uint8)
temp[:,:,0]= img[:,:,0]
#cv2.imshow("blue image", temp)
cv2.imwrite('blue_image.jpg', temp)

temp= np.zeros(img.shape, np.uint8)
temp[:,:,1]= img[:,:,1]
#cv2.imshow("green image", temp)
cv2.imwrite('green_image.jpg', temp)

temp= np.zeros(img.shape, np.uint8)
temp[:,:,2]= img[:,:,2]
#cv2.imshow("red image", temp)
cv2.imwrite('red_image.jpg', temp)

'''
Image Thresholding
'''
img= cv2.imread("demo.jpg", cv2.IMREAD_GRAYSCALE)
img= cv2.GaussianBlur(img, (5,5),0)
threshold, new_img= cv2.threshold(img, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

new_img= cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 2)
#cv2.imshow("thresholding", new_img)
cv2.imwrite('thresholding.jpg', new_img)

'''
save image
'''
#cv2.imwrite('new_image.jpg', new_img)

'''
resize- downscale/upscale
'''
img= cv2.imread("demo.jpg",x)
rescaled_img= cv2.resize(img, (500,500), interpolation= cv2.INTER_LINEAR)
#cv2.imshow("rescaled image", rescaled_img)
cv2.imwrite('rescaled_image.jpg', rescaled_img)
'''
cropping
'''
img= cv2.imread("demo.jpg",x)
cropped_img= img[100:500, 400:600]
#cv2.imshow("cropped image", cropped_img)
cv2.imwrite('cropped_image.jpg', cropped_img)
'''
Rotation
'''
img= cv2.imread("demo.jpg",x)
h,w,_= img.shape
center= w/2, h/2

rotate_matrix= cv2.getRotationMatrix2D(center= center, angle= 45, scale= 1)
rotate_image= cv2.warpAffine(src= img, M= rotate_matrix, dsize= (w,h))
#cv2.imshow("rotated image", rotate_image)
cv2.imwrite('rotated_image.jpg', rotate_image)
'''
Draw shapes
'''
img= cv2.imread("demo.jpg",x)
dup_image= img.copy()
A= (50,50)
B= (50, 300)
cv2.line(dup_image,A, B, (255,255,0), thickness= 3, lineType= cv2.LINE_AA)

C= (400, 50)
D= (50,50)
cv2.line(dup_image,C, D, (0,255,255), thickness= 1, lineType= cv2.LINE_AA)
cc= (int(w/2), int(h/2))
radius= 100
cv2.circle(dup_image, cc, radius, (255,0,255), thickness= 2, lineType= cv2.LINE_4)
text= "skyfall"
pos= (300,300)
cv2.putText(dup_image, text, pos, cv2.FONT_ITALIC, fontScale= 1, color= (0,0,255), thickness= 3, lineType= cv2.LINE_AA)
#cv2.imshow("drawing", dup_image)
cv2.imwrite('drawing.jpg', dup_image)

'''
image segmentation using color spaces
'''
img= cv2.imread("demo.jpg",x)
bgr= [35,56,61]
thresh= 50
maxbgr= np.array([bgr[0]+ thresh, bgr[1]+ thresh, bgr[2]+ thresh])
minbgr= np.array([bgr[0]- thresh, bgr[1]- thresh, bgr[2]- thresh])
maskbgr= cv2.inRange(img, minbgr, maxbgr)
result= cv2.bitwise_and(img, img, mask=maskbgr)

#cv2.imshow("segmented image", result)
cv2.imwrite('segmented_image.jpg', result)
'''
image normalization
'''
img= cv2.imread("demo.jpg",x)
#img_float32= img.astype(np.float32)
normalized_image= cv2.normalize(img, None, -255, 255, cv2.NORM_MINMAX)
#cv2.imshow("Normalized image", normalized_image)
cv2.imwrite('normalized_image.jpg', normalized_image)

'''
add noise
'''
img= cv2.imread("demo.jpg",x)
temp_img= img.copy()
noise= np.random.normal(scale= 0.5, size= img.shape).astype(np.uint8)
noisy_img= cv2.add(temp_img, noise)

#cv2.imshow("noisy image",noisy_img)
cv2.imwrite('noisy_image.jpg', noisy_img)

'''
histogram equalization
'''
img= cv2.imread("demo.jpg",x)
image1= cv2.imread("demo.jpg", cv2.IMREAD_GRAYSCALE)
equalized_img= cv2.equalizeHist(image1)
#cv2.imshow("b/w image",image1)
cv2.imwrite('black_and_white_image.jpg', image1)
#cv2.imshow("equalized image",equalized_img)
cv2.imwrite('equalized_img.jpg', equalized_img)
'''
image convolution
'''
img= cv2.imread("demo.jpg",x)
bin_img= cv2.imread("demo.jpg", cv2.IMREAD_GRAYSCALE)
thres, image2= cv2.threshold(bin_img,127,255, cv2.THRESH_BINARY);
kernel1= np.array([[1,2,1],
                   [0,0,0],
                   [-1,-2,-1]])

kernel2= np.array([[1,0,-1],
                   [2,0,-2],
                   [1,0,-1]])

horizont_edges= cv2.filter2D(src= image2, ddepth= -1, kernel= kernel1)
vertical_edges= cv2.filter2D(src= image2, ddepth= -1, kernel= kernel2)

#cv2.imshow("vertical_edges", vertical_edges)
#cv2.imshow("horizont_edges", horizont_edges)
cv2.imwrite('vertical_edges.jpg', vertical_edges)
cv2.imwrite('horizont_edges.jpg', horizont_edges)

'''
mediun blur
'''
img= cv2.imread("demo.jpg",x)
median= cv2.medianBlur(src= img, ksize= 5)
#cv2.imshow("median blur", median)
cv2.imwrite('median_blur.jpg', median)
'''
sharpen image
'''
img= cv2.imread("demo.jpg",x)
kernel3= np.array([[0,-1,0],
                   [-1,5,-1],
                   [0,-1,0]])

sharp_img= cv2.filter2D(src= img, ddepth= -1, kernel= kernel3)
#cv2.imshow("sharpended image", sharp_img)
cv2.imwrite('sharpended.jpg', sharp_img)

'''
bilateral filter
'''
img= cv2.imread("demo.jpg",x)
bilateral_filter= cv2.bilateralFilter(src= img, d= 9, sigmaColor= 75, sigmaSpace= 75)
#cv2.imshow("bilateral filtered image", bilateral_filter)
cv2.imwrite('bilateral_filtered_image.jpg', bilateral_filter)
'''
canny edge detection
'''
img= cv2.imread("demo.jpg",x)
img_grey= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur= cv2.GaussianBlur(img_grey, (3,3),0)
edge_image= cv2.Canny(image= img_blur, threshold1= 50, threshold2= 150)
#cv2.imshow("edge image", edge_image)
cv2.imwrite('canny_edge_detect.jpg', edge_image)
'''
Contour Detection
'''
img= cv2.imread("demo.jpg",x)
im, thre= cv2.threshold(img_grey, 100,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
contours, heirarchy= cv2.findContours(image= thre, mode= cv2.RETR_TREE, method= cv2.CHAIN_APPROX_NONE)

image_copy= img.copy()

cv2.drawContours(image= image_copy, contours= contours, contourIdx= -1, color= (0,0,255), thickness= 1, lineType= cv2.LINE_AA)
#cv2.imshow("contour lines", image_copy)
cv2.imwrite('contour_lines.jpg', image_copy)
cv2.waitKey(0)
