from sklearn.feature_extraction.text import CountVectorizer;
from sklearn.metrics.pairwise import euclidean_distances

corpus=[
    'My name is Anish',
    'Anish',
    'name is anish'
]

vectorized=CountVectorizer();
x=vectorized.fit_transform(corpus);
print(vectorized.get_feature_names());
value=x.toarray()
print(value)
print(euclidean_distances(value[0],value[1]))