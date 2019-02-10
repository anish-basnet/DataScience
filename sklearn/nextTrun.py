from sklearn.linear_model import LinearRegression;

x=[[6],[8],[10],[14],[18]];
y=[[7],[9],[13],[17.5],[18]];

model=LinearRegression();
model.fit(x,y);
print("A 12 diameter pizza should cost at least of %.2f$" %model.predict([[12]])[0][0]);