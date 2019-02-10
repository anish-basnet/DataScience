import pandas as pd
from sklearn.tree import DecisionTreeRegressor;

file=pd.read_csv("../data/melb_data.csv");
y=file.Price;
x=file[['Rooms','Bathroom','Landsize','Lattitude','Longtitude']];
model=DecisionTreeRegressor(random_state=1);
model.fit(x,y);
print(x.head());
print(model.predict(x.head()));