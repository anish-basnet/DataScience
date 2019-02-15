from sklearn.feature_extraction.text import HashingVectorizer;
from nltk import word_tokenize

corpus=[
    'Anish Basnet anish',
]
print(word_tokenize(corpus[0]))
vector=HashingVectorizer(n_features=5);
print(vector.fit_transform(word_tokenize(corpus[0])).todense());