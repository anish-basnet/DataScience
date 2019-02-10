import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;
from sklearn.linear_model import LinearRegression;
from sklearn.model_selection import train_test_split,cross_val_score;

data=pd.read_csv('../data/winequality-red.csv',sep=';');
X=data[list(data.columns)[:-1]]
Y=data['quality'];
x_train,x_test,y_train,y_test=train_test_split(X,Y);
regression=LinearRegression();

