from nltk.stem.porter import PorterStemmer;
from nltk.stem.lancaster import LancasterStemmer;
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize

porter=PorterStemmer();
lanchaster=LancasterStemmer();
wordnet=WordNetLemmatizer();


words=['welcome','didnot','willnot','found','false','random'];
print('{0:20}{1:20}{2:20}{3:20}'.format('words','Porter Steammer','Lancaster Steammer','Word Net Lammentizer'));
for x in words:
    print('{0:20}{1:20}{2:20}{3:20}'.format(x,porter.stem(x),lanchaster.stem(x),wordnet.lemmatize(x)))

print(word_tokenize('Welcome to the anish world command center.'))