from nltk import FreqDist
from nltk.corpus import stopwords, brown

# Write a function that finds the 50 most frequently occurring words of a text that are not stopwords.
en_sw = stopwords.words('english')


# def top50words_nostop(wordlist):
# 	'''return the top 50 words that are not stopwords'''
# 	# fdist = FreqDist([w.lower() for w in wordlist])
# 	# return sorted([word for word in fdist.keys() if word not in en_sw and word.isalpha()], reverse=True, key=lambda x: fdist[x])[:50]
# 	return FreqDist([w.lower() for w in wordlist if w.isalpha() and w not in en_sw]).most_common(50)

def top50_nostop(wordlist):
	most_common = FreqDist([w.lower() for w in wordlist if (w.isalpha() or w.isdigit()) and w not in en_sw]).most_common(50) 
	w_col1 = max([len(w[0]) for w in most_common])
	w_col2 = len(str(max([w[1] for w in most_common])))
	for i,word_info in enumerate(most_common):
		# print "word: {0}  occurrences: {1}".format(word,occur)
		word, occur = word_info
		print "{0:<3} |{1:<{col1}}|{2:<{col2}}".format(i,word,occur,col1=w_col1,col2=w_col2)


if __name__ == "__main__":
	top50_nostop(brown.words())

