import nltk
import numpy as np
# nltk.download('punkt')

from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sen, all_words):
    tokenized_sen = [stem(w) for w in tokenized_sen]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_sen:
            bag[idx] = 1.0
    return bag

# a = "How long does shippin take?"
# print(a)
# a = tokenize(a)
# print(a)
# words = ["organize", "organizes","organizing"]
# stemmed_words = [stem(w) for w in words]
# print(stemmed_words)