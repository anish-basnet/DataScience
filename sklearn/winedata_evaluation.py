from sklearn.linear_model import LinearRegression;
import pandas as pd;

data=pd.read_csv('../data/winequality-red.csv',sep=';');
x=data[list(data.columns[:-1])];
y=data['quality'];
model=LinearRegression();
model.fit(x,y);
