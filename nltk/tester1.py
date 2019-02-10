from nltk.tokenize import word_tokenize,WordPunctTokenizer,sent_tokenize;

input_txt="Do you know what is tokenize? I know i love u lot but i don't know wheather you love me or not.";

print("Sentence Tokenize : ");
print(sent_tokenize(input_txt))

print('Word Tokenize  : ');
print(WordPunctTokenizer().tokenize(input_txt));