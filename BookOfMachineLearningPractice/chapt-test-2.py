from sklearn.linear_model import LinearRegression;
import numpy as np;

x=[[6],[8],[10],[14],[18]];
y=[[7],[9],[13],[17.5],[18]];

model=LinearRegression();
model.fit(x,y);

print("The 12\" Diameter pizza can cost you around $%.2f" %(model.predict([[18]])[0][0]));


#testing myself

test_x=[[12],[30],[23],[9]];
print(model.predict(test_x));

error=np.mean((model.predict(x)-y)**2);
print("residual error ",error);