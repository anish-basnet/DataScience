from sklearn.linear_model import LinearRegression;
from sklearn.preprocessing import PolynomialFeatures;
import matplotlib.pyplot as plt;
import numpy as np;


x_train=[[6],[8],[10],[14],[18]];
y_train=[[7],[9],[13],[17.5],[18]];

x_test=[[6],[8],[10],[14]];
y_test=[[7],[9],[13],[17.5]];

#training the model with normal regression
normal_regression=LinearRegression();
normal_regression.fit(x_train,y_train);

#creating the random line with regression
xx=np.linspace(0,26,100);
yy=normal_regression.predict(xx.reshape(xx.shape[0],1));

plt.plot(xx,yy);

#creating polynomial feature dataset from train
poly=PolynomialFeatures(degree=5);

x_quad_train=poly.fit_transform(x_train);

quad_regression=LinearRegression();
quad_regression.fit(x_quad_train,y_train);

xx_quad=poly.transform(xx.reshape(xx.shape[0],1));
yy_quad=quad_regression.predict(xx_quad);

plt.plot(xx_quad,yy_quad,c='r',linestyle='--');

plt.scatter(x_train,y_train);
plt.axis([0,25,0,25])
plt.grid(True)
print("R-sq of Normal : ",normal_regression.score(x_train,y_train));
print("R-sq of Qurd : ", quad_regression.score(x_quad_train,y_train));

plt.show();

xx_test_quad=poly.fit_transform(x_test);
print(quad_regression.predict(xx_test_quad));
print("R-sq of Test Qurd : ",quad_regression.score(xx_test_quad,y_test));