from sklearn.linear_model import LinearRegression;
import numpy as np;
import matplotlib.pyplot as plt;


X=[[8],[9],[11],[16],[12]];
y=[[11],[8.5],[15],[18],[11]];

model=LinearRegression();
model.fit(X,y);

predict_y=model.predict(X);
print(predict_y);

print("R square is ",model.score(X,predict_y));