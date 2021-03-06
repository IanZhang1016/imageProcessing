import cv2


def a5(path):
    img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)#read a binary image
    rows, cols = img.shape  #get the rows and columns of the grey image
    
    feature = [[0]*3 for i in range(3)] #feature vector
    zoneR=rows//3
    zoneC=cols//3
    for i in range(3):
        for j in range(3):
            black=0
            white=0
            for r in range(i*zoneR,(i+1)*zoneR):
                for c in range(j*zoneC,(j+1)*zoneC):
                    if(img[r][c] == 0):#black pixel
                        black += 1
                    elif(img[r][c] == 255):
                        white += 1
            feature[i][j]=black/white
    fo = open('res/a5/feature.txt', "w")
    for ip in feature:
        fo.write(str(ip))
        fo.write('\n')
    fo.write('\n')

    fo.close()
    print(feature)
    cv2.waitKey(0)
    cv2.destroyAllWindows()