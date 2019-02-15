from nltk import word_tokenize,pos_tag;
from nltk.stem import PorterStemmer;
from nltk.stem.wordnet import WordNetLemmatizer;


corpus=[
    'He ate the sandwitches',
    'Every sandwitch was eaten by him',
    'he asked me to purpose you'
];

steamer=PorterStemmer();
print('Stemmed : ',[[steamer.stem(x) for x in word_tokenize(doc)] for doc in corpus]);
tagged_corpos=[pos_tag(word_tokenize(doc)) for doc in corpus];
print(tagged_corpos)

lammentizer=WordNetLemmatizer();
def lemenntize(token,tag):
    if(tag[0].lower() in ['n','v']):
        return lammentizer.lemmatize(token,tag[0].lower());
    return token;

print('Lemmentize : ',[[lemenntize(token,tag) for token,tag in document]for document in tagged_corpos])