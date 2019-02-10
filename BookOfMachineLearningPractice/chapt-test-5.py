from sklearn.linear_model import LinearRegression;
from sklearn.preprocessing import PolynomialFeatures;
import matplotlib.pyplot as plt;
import numpy as np;


x_train=[[6],[8],[10],[14],[18]];
y_train=[[7],[9],[13],[17.5],[18]];

x_test=[[6],[8],[10],[14]];
y_test=[[7],[9],[13],[17.5]];

regressor=LinearRegression();
regressor.fit(x_train,y_train);

xx=np.linspace(0,26,100);
yy=regressor.predict(xx.reshape(xx.shape[0],1));
plt.plot(xx,yy);
#plt.show


quad_feature=PolynomialFeatures(degree=2);
x_train_quad=quad_feature.fit_transform(x_train);
x_test_quad=quad_feature.transform(x_test);

quad_regressor=LinearRegression();
quad_regressor.fit(x_train_quad,y_train);

xx_quad=quad_feature.fit_transform(xx.reshape(xx.shape[0],1));

plt.plot(xx,quad_regressor.predict(xx_quad),c='r',linestyle='--');
plt.scatter(x_train,y_train);


print("R-sq of normal : ",regressor.score(x_train,y_train));
print("R-sq of poly : ",quad_regressor.score(x_train_quad,y_train));
plt.show();
