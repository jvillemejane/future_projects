# -*- coding: utf-8 -*-
"""*11_opencv_object_detect* file.

.. note:: LEnsE - Institut d'Optique - version 0.1

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

@see https://www.geeksforgeeks.org/detect-an-object-with-opencv-python/
@see https://www.analyticsvidhya.com/blog/2021/05/image-processing-using-opencv-with-practical-examples/

@see for FC : https://pyimagesearch.com/2016/02/01/opencv-center-of-contour/
@see for FC : https://pyimagesearch.com/2016/02/08/opencv-shape-detection/
@see https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html

Industrial Applications
@see https://patrick-bonnin.developpez.com/cours/vision/apprendre-bases-traitement-image/partie-5-segmentation-contour/
"""

import cv2 as cv
import imutils
import numpy as np

# Open and display image
import cv2
from matplotlib import pyplot as plt


# Opening image
img = cv2.imread("../../../_data/formes.png")
img_cpy = img.copy()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur_size = 3
blurred = cv2.GaussianBlur(gray, (blur_size, blur_size), 0)
thresh = cv2.threshold(blurred, 180, 255, cv2.THRESH_BINARY)[1]

# find contours in the threshold image
contours_cnts = cv2.findContours(thresh.copy(), cv2.RETR_TREE,
	cv2.CHAIN_APPROX_SIMPLE)
contours_cnts = imutils.grab_contours(contours_cnts)

print(f'Contours count = {len(contours_cnts)}')
cnt = contours_cnts[3]

cv.drawContours(img, cnt, -1, (0,255,0), 3)

plt.figure()
plt.imshow(img)
plt.show()

'''
for idx, c in enumerate(contours_cnts):
    # compute the center of the contour
    M = cv2.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    # draw the contour and center of the shape on the image
    cv2.drawContours(img_cpy, [c], -1, (0, 255, 0), 2)
    cv2.circle(img_cpy, (cX, cY), 4, (255, 255, 255), -1)
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    # show the image
    cv2.imshow("Image", img)
    cv2.waitKey(0)

'''
