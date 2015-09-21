import nltk
from nltk.corpus import stopwords, brown
import string

import timeit



en_sw = stopwords.words("english")

text = [w.lower() for w in brown.words()] #lower all text in brown corpus
bigrams = nltk.bigrams(text)
cfd = nltk.ConditionalFreqDist(bigrams)

#flattening dictionary produced by cfd into list
l = [(w1, w2, cfd[w1][w2]) for w1 in cfd.keys() for w2 in cfd[w1].keys()]

#filter out all bigrams with stop words and punctuation
def not_stop_or_punc(bigram_tuple):
	w1,w2,count = bigram_tuple
	return (w1.isalpha() and w1 not in en_sw) and (w2.isalpha() and w2 not in en_sw)
	
#sort by count of bigram and filter out punctuation and stop words
#filter after sorting
# for w1,w2,count in filter(not_stop_or_punc,sorted(l,key=lambda x: x[2], reverse=True))[:50]: 
# 	print "bigram ({},{}) occured count {}".format(w1,w2,count)


#filter before sorting
for w1,w2,count in sorted(filter(not_stop_or_punc,l),key=lambda x: x[2], reverse=True)[:50]:
	print "bigram ({},{}) occured count {}".format(w1,w2,count)	

