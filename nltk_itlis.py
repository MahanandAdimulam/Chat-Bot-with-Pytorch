import nltk
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sen, all_words):
    pass

a = "How long does shippin take?"
print(a)
a = tokenize(a)
print(a)