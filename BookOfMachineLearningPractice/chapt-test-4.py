from sklearn.linear_model import LinearRegression;
import numpy as np;


train_x=[[6,2],[8,1],[10,0],[14,2],[18,0]];
train_y=[[7],[9],[13],[17.5],[18]];

test_x=[[8,2],[9,0],[11,2],[16,2],[12,0]];
test_y=[[11],[8.5],[15],[18],[11]];

model=LinearRegression();

model.fit(train_x,train_y);



print(model.predict(test_x));

print("R-square : ",model.score(test_x,test_y));


prediction=model.predict(test_x);

for i,prediction in enumerate(prediction):
    print("Prediction : %s target : %s" %(prediction,test_y[i]));
print("R-sq : ",model.score(test_x,test_y));