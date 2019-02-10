import pandas as pd;
from sklearn.feature_extraction.text import CountVectorizer;
from sklearn.metrics import euclidean_distances;

corpus=[
    'UNC played Duke in basketball',
    'Duke lost the basketball game',
    'I ate sandwitch'
];


vectorize=CountVectorizer();
val=vectorize.fit_transform(corpus);
print(val.toarray());
print(vectorize.vocabulary_)