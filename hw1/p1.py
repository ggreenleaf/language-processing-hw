from nltk import FreqDist
from nltk.corpus import brown

#first we remove all words that don't contain either a digit or a number 
#before running FreqDist
fdist = FreqDist(word.lower() for word in brown.words() if any(c.isalpha() or c.isdigit() for c in word))
print  len([word for word in fdist.keys() if fdist[word] >= 3])



