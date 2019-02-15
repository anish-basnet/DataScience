from skimage.color import rgb2gray;
import matplotlib.pyplot as plt;
import numpy as np;
from skimage.feature import corner_harris,corner_peaks;
import skimage.io as io;
from skimage.exposure import equalize_hist;

def show_corners(corner,image):
    fig=plt.figure();
    plt.gray();
    plt.imshow(image);
    x_corner,y_corner=zip(*corner);
    plt.plot(x_corner,y_corner);
    plt.xlim(0,image.shape[1]);
    plt.ylim(image.shape[0],0)
    fig.set
    plt.show()


mandrill=io.imread('../data/mandrill.png');
mandrill=equalize_hist(rgb2gray(mandrill));
corner=corner_peaks(corner_harris(mandrill),min_distance=2);
print(corner);
show_corners(corner,mandrill)