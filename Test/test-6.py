from nltk import sent_tokenize,pos_tag,word_tokenize;
from nltk.stem import PorterStemmer;
from sklearn.feature_extraction.text import CountVectorizer;
from nltk.stem.wordnet import WordNetLemmatizer;
from sklearn import preprocessing;

f=open('../data/analysis.txt','r');
txt=f.read()
sentences=sent_tokenize(txt);

key_word=['n','v'];
count=CountVectorizer();

data=count.fit_transform(sentences).todense();
print(preprocessing.scale(data))

stemmer=PorterStemmer();
print("Steammed Text : ",[[x for x in word_tokenize(doc)] for doc in sentences])

lammentizer=WordNetLemmatizer();

def lemmentize(token,tag):
    if(tag[0].lower() in key_word):
        return lammentizer.lemmatize(token,tag[0].lower());
    return token;

tagged_words=[pos_tag(word_tokenize(x)) for x in sentences];
print("Refined Text : ",[[lemmentize(token,tag) for token,tag in doc] for doc in tagged_words])
