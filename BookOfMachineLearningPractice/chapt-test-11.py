from sklearn.datasets import load_digits;
import matplotlib.pyplot as plt;
digits=load_digits();
print("Digit : ",digits.target[0])
print("Image : ",digits.images[0])
print("Featured Vector : \n",digits.images[0].reshape(-1,64))
plt.imshow(digits.images[1])
plt.show()