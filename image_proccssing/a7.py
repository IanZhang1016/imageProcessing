# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 11:48:28 2018

@author: Ian Zhang
"""

import numpy as np
from skimage import io
import PIL.Image


def get_cluster_mean_point(cluster):
    cluster_array = np.array(cluster)
    return np.mean(cluster_array,axis=0)


def get_euclidean_distance(mean_point_fir, mean_point_sec):     
    dist = np.linalg.norm(mean_point_fir-mean_point_sec)

    return dist
    

def find_nearest_cluster(cluster_list):
    smallest_distance = 99999999
    smallest_cluster_fir = -1
    smallest_cluster_sec = -1
    
    for first,cluster_fir in enumerate(cluster_list):
        for second,cluster_sec in enumerate(cluster_list):
            if first != second:
                mean_point_fir = get_cluster_mean_point(cluster_fir)
                mean_point_sec = get_cluster_mean_point(cluster_sec)
                dist = get_euclidean_distance(mean_point_fir, mean_point_sec)
                if dist < smallest_distance:
                    smallest_distance = dist
                    smallest_cluster_fir = first
                    smallest_cluster_sec = second
    cluster_list[smallest_cluster_sec].extend(cluster_list[smallest_cluster_fir])
    cluster_list.pop(smallest_cluster_fir)


def get_point_cluster(picture):
    point_list = []
    for x,row in enumerate(picture):
        for y,point in enumerate(row):
            if point == 0:
                point_list.append([[x,y]])
    return point_list


def generate_seperate_img(cluster_list,save_path):
    for i,cluster in enumerate(cluster_list):
        cluster_array = np.array(cluster)
        shape = np.max(cluster_array,axis=0)
        new_img_array = np.full((shape[0]+1,shape[1]+1),255,dtype=np.uint8)
        for point in cluster:
            new_img_array[point[0]][point[1]] = 0
        new_img = PIL.Image.fromarray(new_img_array)
        new_img.save(save_path+str(i)+'.jpg')


def processImg(path):
    im = io.imread(path)
    rows, cols = im.shape
    for r in range(rows):
        for c in range(cols):
            if (im[r, c] >= 128):
                im[r, c] = 255
            else:
                im[r, c] = 0
    return im


def find_cluster(pic,num_of_symbol=2,save_path='res/a7/'):
    cluster_list = get_point_cluster(processImg(pic))
    
    while len(cluster_list) > num_of_symbol:
        find_nearest_cluster(cluster_list)
    
    generate_seperate_img(cluster_list,save_path)
    print('Success')



def main():

    find_cluster('../res/a4/resize_img.jpg',2)
    

if __name__ == '__main__':
    main()