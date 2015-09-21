from nltk import FreqDist
from nltk.corpus import brown

#remove all nonalpha words and make lowercase
fdist = FreqDist(word.lower() for word in brown.words() if word.isalpha() or word.isdigit()) #use lowercase of words to avoid duplicates like The and the
print  len([word for word in fdist.keys() if fdist[word] >= 3])



