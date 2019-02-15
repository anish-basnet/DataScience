from nltk.stem import PorterStemmer;
from nltk.stem.wordnet import WordNetLemmatizer;
from nltk import pos_tag,word_tokenize;

corpus=[
    'He ate sandwich',
    'Every boy likes to eat sandwich'
]

steamer=PorterStemmer();

print("Steammed : ",[[x for x in word_tokenize(doc)] for doc in corpus])

tagged=[pos_tag(word_tokenize(x)) for x in corpus];

lammet=WordNetLemmatizer();
def lammentize(token,tag):
    if(tag[0].lower() in ['n','v']):
        return lammet.lemmatize(token,tag[0].lower())
    return token;

print("Refined : ",[[lammentize(token,tag) for token,tag in doc] for doc in tagged])