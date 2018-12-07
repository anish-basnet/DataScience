import pandas as pd;
import numpy as np;

data={'val1':pd.Series([1,2,3,4,5,6,7,8,9,10]),'val2':pd.Series([2,3,2,3,3,4,4,2,3,4])};
d=pd.DataFrame(data);
print(pd.get_option('display.max_rows'));