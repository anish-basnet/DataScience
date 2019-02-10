from sklearn.linear_model import LinearRegression;
from sklearn.model_selection import cross_val_score,train_test_split;
from sklearn.preprocessing import PolynomialFeatures;
import pandas as pd;

data=pd.read_csv("../data/iris.data.txt");
x=data[list(data.columns)[:-2]];
y=data[list(data.columns)[-2]];

poly=PolynomialFeatures(degree=3);
x_quad=poly.fit_transform(x);

model=LinearRegression();
model.fit(x_quad,y);

print(model.predict(x_quad));
print(model.score(x_quad,y));