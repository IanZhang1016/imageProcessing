import cv2


def a6(path):
    fo = open(path, "w")
    for i in range(10):
        name = 'res/a6/6-'+str(i)+'.jpg'
        img = cv2.imread(name, cv2.IMREAD_GRAYSCALE)  # read a gray image number i
        rows, cols = img.shape  # get the rows and columns of the grey image
    
        feature = [[0]*3 for i in range(3)] #feature vector
        zoneR = rows//3
        zoneC = cols//3
        for j in range(3):
             for k in range(3):
                black=0
                white=0
                for r in range(j*zoneR,(j+1)*zoneR):
                    for c in range(k*zoneC,(k+1)*zoneC):
                        if(img[r][c] < 178):#black pixel
                            black += 1
                        else:
                            white += 1
                feature[j][k]=black/white
        for ip in feature:
             fo.write(str(ip))
             fo.write('\n')
        fo.write('\n')
    
    fo.close()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
