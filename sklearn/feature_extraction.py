from sklearn.feature_extraction.text import TfidfVectorizer;

corpus=['Welcome to the anish world command center so many people working here',
        'welcome to miami'];
vectorized=TfidfVectorizer(stop_words='english')
print(vectorized.fit_transform(corpus).todense());
print(vectorized.vocabulary_);