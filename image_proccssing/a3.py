import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage import io
from skimage.color import rgb2gray
from skimage import img_as_ubyte


def conv(image, kernel):
    rows, cols = image.shape
    krows, kcols = kernel.shape
    #rev_m = np.zeros((Hkernel,Wkernel))

    cal_img = np.empty(shape=(rows + 2, cols + 2), dtype=int)
    cal_img[:cols + 2] = 0

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            cal_img[i, j] = image[i - 1, j - 1]

    cal_slice = np.empty(shape=(krows, kcols), dtype=int)

    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            for i in range(krows):
                for j in range(kcols):
                    cal_slice[i, j] = cal_img[r + i - 1, c + j - 1]
            cal_slice = cal_slice * kernel
            a = np.sum(cal_slice)
            if (a < 0):
                a = 0
            elif (a > 255):
                a = 255
            image[r - 1][c - 1] = a
    return image

    # Himage, Wimage = image.shape
    # Hkernel, Wkernel = kernel.shape
    # rev_m = np.zeros((Hkernel,Wkernel))
    # for m in range(Hkernel):
    #     for n in range(Wkernel):
    #         rev_m[m][n] = kernel[Hkernel-1-m][Wkernel-1-n]
    # kernel = rev_m
    # temp_m = np.zeros((Himage+Hkernel-1, Wimage+Wkernel-1))
    #
    # for i in range(Himage+Hkernel-1):
    #     for j in range(Wimage+Wkernel-1):
    #         temp = 0
    #         for m in range(Hkernel):
    #             for n in range(Wkernel):
    #                 if ((i-m)>=0 and (i-m)<Himage and (j-n)>=0 and (j-n)<Wimage):
    #                     temp += image[i-m][j-n] * kernel[m][n]
    #         temp_m[i][j] = temp
    # return temp_m


def a3(path):
    img = io.imread(path)  ##read the image file
    grey = rgb2gray(img)  ##change rgb image to grey image
    image = img_as_ubyte(grey)
    #image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)  # read as gray image
    matrix1 = np.array([[1/3,1/3,1/3]])
    matrix2 = np.array([[1/3],
                       [1/3],
                       [1/3]])
    matrixtest = np.array([[1/9,1/9,1/9],
                      [1/9,1/9,1/9],
                      [1/9,1/9,1/9]])
    
    temp = conv(image, matrix1)
    res = conv(temp, matrix2)
    io.imsave('res/a3/a3.jpg', res)  ##save the grey image for your disk  path:the source file path/unfilteredImg.jpg
    return 'res/a3/a3.jpg'










