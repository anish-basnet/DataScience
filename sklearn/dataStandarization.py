import numpy as np;
from sklearn import preprocessing;

array=np.array([[1,2,3,4,5]],dtype=float);
print(preprocessing.scale(array));