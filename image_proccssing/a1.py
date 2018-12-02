# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 23:56:35 2018

@author: 逸阳
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from skimage import io
from skimage.color import rgb2gray
from skimage import img_as_ubyte
import numpy as np


def cov_img(path):
    img = io.imread(path) ##read the image file
    grey = rgb2gray(img)  ##change rgb image to grey image
    dst_img = img_as_ubyte(grey)
    io.imsave('res/a1/unfilteredImg.jpg', dst_img)   ##save the grey image for your disk  path:the source file path/unfilteredImg.jpg
    rows, cols = dst_img.shape  ##get the rows and columns from the grey image
    
    kernel = np.array([(-1,-1,-1),(-1,9,-1),(-1,-1,-1)])  #set convolution kernel
    
    cal_img = np.empty(shape = (rows + 2, cols + 2), dtype = int)
    cal_img[:cols + 2] = 0
    
    
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            cal_img[i, j] = dst_img[i - 1, j - 1]
    
    cal_slice = np.empty(shape = (3, 3), dtype = int)
    
    for r in range(1, rows + 1):
       for c in range(1, cols + 1):
           for i in range(3):
               for j in range(3):
                   cal_slice[i, j] = cal_img[r + i - 1, c + j - 1]
           cal_slice = cal_slice * kernel   
           a = np.sum(cal_slice)
           if(a < 0):
               a = 0
           elif(a > 255):
               a = 255
           dst_img[r - 1][c - 1] = a
    io.imshow(dst_img) 
    io.imsave('res/a1/filteredImg.jpg',dst_img)  ##write the processed image into your disk  path:the source file path/filteredImg.jpg

    return 'res/a1/filteredImg.jpg'