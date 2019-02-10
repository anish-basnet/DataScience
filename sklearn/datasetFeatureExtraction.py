from sklearn import datasets;

image=datasets.load_digits();
print('digits : ',image.target[0]);
print(image.images[0]);
print(image.images[0].reshape(1,64));