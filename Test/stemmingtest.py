from nltk.stem.porter import PorterStemmer;
from nltk.stem.lancaster import LancasterStemmer;
from nltk.stem.wordnet import WordNetLemmatizer;

porter=WordNetLemmatizer();
lancaster=LancasterStemmer();



words=['stem','working','world','worked','missing','missed','male'];
print('{0:20}{1:20}{2:20}'.format('Words','Porter Stemmer','Lancaster Steammer'));
for word in words:
    print('{0:20}{1:20}{2:20}'.format(word,porter.lemmatize(word),lancaster.stem(word)));