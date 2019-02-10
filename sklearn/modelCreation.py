import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

input_txt=pd.read_csv("../household data/train.csv");
test_txt=pd.read_csv("../household data/test.csv");

y=input_txt.SalePrice;
label=['LotArea','YearBuilt','1stFlrSF','2ndFlrSF','FullBath','BedroomAbvGr','TotRmsAbvGrd'];
x=input_txt[label];

train_x,val_x,train_y,val_y=train_test_split(x,y,random_state=0);
model=DecisionTreeRegressor();

#test_x=test_txt[label];
model.fit(train_x,train_y);




predicted=model.predict(val_x)
print(mean_absolute_error(val_y,predicted))