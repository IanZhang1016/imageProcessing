from skimage import morphology,data,color
import matplotlib.pyplot as plt
from skimage import io


def a8(path):

    image = io.imread(path)  ##read the image file
    rows, cols = image.shape
    for r in range(rows):
        for c in range(cols):
            if (image[r, c] >= 128):
                image[r, c] = True
            else:
                image[r, c] = False
    image=1-image #反相
    #实施骨架算法
    skeleton =morphology.skeletonize(image)

    
    #显示结果
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
    
    ax1.imshow(image, cmap=plt.cm.gray)
    ax1.axis('off')
    ax1.set_title('original', fontsize=20)
    
    ax2.imshow(skeleton, cmap=plt.cm.gray)
    ax2.axis('off')
    ax2.set_title('skeleton', fontsize=20)
    
    fig.tight_layout()
    plt.show()
