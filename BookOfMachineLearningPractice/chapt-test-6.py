import numpy as np;
from sklearn.linear_model import SGDRegressor;
from sklearn.datasets import load_boston;
from sklearn.preprocessing import StandardScaler;
from sklearn.model_selection import cross_val_score,train_test_split;

data=load_boston();
x_train,x_test,y_train,y_test=train_test_split(data.data,data.target);

y_t=np.reshape(y_train,newshape=[len(y_train),1]);
y_te=np.reshape(y_test,newshape=[len(y_test),1]);

x_scaler=StandardScaler();
y_scaler=StandardScaler();

x_train_evo=x_scaler.fit_transform(x_train);
y_train_evo=y_scaler.fit_transform(y_t);


x_test_evo=x_scaler.transform(x_test);
y_test_evo=y_scaler.transform(y_te);

regression=SGDRegressor(loss='squared_loss');
score=cross_val_score(regression,x_train_evo,y_train_evo,cv=5);

print(score)
print(np.mean(score))

regression.fit(x_train_evo,y_train_evo);
print(regression.score(x_test_evo,y_test_evo))