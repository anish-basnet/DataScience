import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;

data=pd.read_csv('../data/winequality-red.csv',sep=';');
da=data.describe();
print(da);
plt.scatter(da['volatile acidity'],da['quality']);
plt.xlabel("volatile Acidity");
plt.ylabel("Quality");
plt.title("Alcohol against quality");
plt.show();