from nltk import FreqDist
from nltk.corpus import brown

# Write a program to find all words that occur at least three times in the Brown Corpus.
#remove all non alpha words such as . , !. and make all words lowercase
fdist = FreqDist(word.lower() for word in brown.words() if word.isalpha()) #use lowercase of words to avoid duplicates like The and the
print  len([word for word in fdist.keys() if fdist[word] >= 3])



