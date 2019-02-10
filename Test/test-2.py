import pandas as pd;
from sklearn.preprocessing import PolynomialFeatures;
from sklearn.linear_model import LinearRegression;
from sklearn.model_selection import train_test_split,cross_val_score;



data=pd.read_csv('../data/winequality-red.csv',sep=';');

#access the data
X=data[list(data.columns)[:-1]];
Y=data['quality'];

#spliting test and training data
x_train,x_test,y_train,y_test=train_test_split(X,Y);



#model declaration
model=LinearRegression();
model.fit(x_train,y_train);

score=cross_val_score(model,X,Y,cv=10);
print(score);

print(model.score(x_test,y_test));