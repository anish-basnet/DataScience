from sklearn.linear_model import LinearRegression;
from sklearn.feature_extraction import dict_vectorizer;
from sklearn.model_selection import cross_val_score,train_test_split;
import pandas as pd;

data=pd.read_csv("../data/iris.data.txt");
x=data[list(data.columns)[:-2]];
y=data[list(data.columns)[-2]];
x_train,x_test,y_train,y_test=train_test_split(x,y);
model=LinearRegression();
model.fit(x_train,y_train);
prediction=model.predict(x_test);
print(prediction);