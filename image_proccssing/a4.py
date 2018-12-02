# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 15:20:35 2018

@author: Ian
"""
import numpy as np
import PIL.Image
import scipy.misc


def resize_Image(picture_path=None):
    if picture_path is None:
        raise ValueError('File Path Error')

    im = PIL.Image.open(picture_path)
    im_mat = scipy.misc.fromimage(im)
    width = 20
    length = int((width/im.size[0]) * im.size[1])
    im_mat_resized = np.empty((length, width), dtype=np.uint8)

    for r in range(im_mat_resized.shape[0]):
        for c in range(im_mat_resized.shape[1]):
            rr = (r + 1) / im_mat_resized.shape[0] * im_mat.shape[0] - 1
            cc = (c + 1) / im_mat_resized.shape[1] * im_mat.shape[1] - 1

            rr_int = int(rr)
            cc_int = int(cc)

            if rr == rr_int and cc == cc_int:
                p = im_mat[rr_int][cc_int]
            elif rr == rr_int:
                p = im_mat[rr_int][cc_int] * (cc_int + 1 - cc) + im_mat[rr_int][cc_int + 1] * (cc - cc_int)
            elif cc == cc_int:
                p = im_mat[rr_int][cc_int] * (rr_int + 1 - rr) + im_mat[rr_int + 1][cc_int] * (rr - rr_int)
            else:
                p11 = (rr_int, cc_int)
                p12 = (rr_int, cc_int + 1)
                p21 = (rr_int + 1, cc_int)
                p22 = (rr_int + 1, cc_int + 1)

                dr1 = rr - rr_int
                dr2 = rr_int + 1 - rr
                dc1 = cc - cc_int
                dc2 = cc_int + 1 - cc

                w11 = dr2 * dc2
                w12 = dr2 * dc1
                w21 = dr1 * dc2
                w22 = dr1 * dc1

                p = im_mat[p11[0]][p11[1]] * w11 + im_mat[p21[0]][p21[1]] * w12 + \
                    im_mat[p12[0]][p12[1]] * w21 + im_mat[p22[0]][p22[1]] * w22

            im_mat_resized[r][c] = p

    im_resized = PIL.Image.fromarray(im_mat_resized)
    ##im_resized.show()
    im_resized.save('res/a4/resize_img.jpg')
    return 'res/a4/resize_img.jpg'
    
def main():
    resize_Image()


if __name__ == '__main__':
    main()    
