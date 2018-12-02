import cv2
from skimage import measure


def a2(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)#read as gray image
    rows, cols = img.shape  #get the rows and columns of the grey image
    
    for r in range(rows):
        for c in range(cols):
            if(img[r][c]>=178):
                img[r][c]=255
            else:
                img[r][c]=0
    #cv2.imshow("2-result2",img)
    cv2.imwrite('res/a2/a5.jpg', img)#the image for a5
    labeled_img, num = measure.label(img, neighbors=8, background=255, return_num=True)
    props = measure.regionprops(labeled_img)
    fo = open('res/a2/record.txt', "w")

    fo.write(str("region\t#pixels"))
    fo.write('\n')
    for i in range(0, num):
        fo.write(str(i+1)+"\t\t"+str(props[i].area))
        fo.write('\n')
    fo.close()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 'res/a2/a5.jpg'



