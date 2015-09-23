import nltk
from nltk.corpus import stopwords, brown

def top50_bigrams_nostop(wordlist):
	en_sw = stopwords.words("english")
	text = [w.lower() for w in wordlist] #lower all text in brown corpus
	bigrams = nltk.bigrams(text)
	cfd = nltk.ConditionalFreqDist(bigrams)

	#flattening dictionary produced by ConditionalFeqDist into list
	l = [(w1, w2, cfd[w1][w2]) for w1 in cfd.keys() for w2 in cfd[w1].keys()]

	def not_stop_or_punc(bigram):
		'''returns true if bigram is not a stopword and not a punctuation mark'''
		w1,w2,count = bigram
	
		#if both words do not contain a digit or alpha and not in stopwords
		return ((any(c.isalpha() or c.isdigit() for c in w1) and w1 not in en_sw) and 
				(any(c.isalpha() or c.isdigit() for c in w2) and w2 not in en_sw))
		
	
	#filter then sort bigrams
	most_common = sorted(filter(not_stop_or_punc,l),key=lambda x: x[2], reverse=True)[:50]

	col1 = max([len(w1+w2) for w1,w2,count in most_common])  #longest bigram
	col2 = max([len(str(count)) for w1,w2,count in most_common]) #length of the digit with largest numbers

	#displaying the most common
	for i,word_info in enumerate(most_common):
		w1,w2,count = word_info
		print "{0:<3}| {w:<{col1}}|{c:<{col2}}".format(i,w=w1+" " +w2,c=count,col1=col1+1,col2=col2)


if __name__ == "__main__":
	top50_bigrams_nostop(brown.words())