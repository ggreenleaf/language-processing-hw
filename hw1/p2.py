from nltk import FreqDist
from nltk.corpus import stopwords, brown

# Write a function that finds the 50 most frequently occurring words of a text that are not stopwords.



def top50_nostop(wordlist):
	'''print the top 50 words that are not stop words from wordlist'''
	# most_common = FreqDist([w.lower() for w in wordlist if (w.isalpha() or w.isdigit()) and w.lower() not in en_sw]).most_common(50) 	
	en_sw = stopwords.words('english')
	
	text = [w.lower() for w in wordlist if w.lower() not in en_sw and any(c.isalpha() or c.isdigit() for c in w)]
	most_common = FreqDist(text).most_common(50)

	#displaying words
	w_col1 = max([len(w[0]) for w in most_common])
	w_col2 = len(str(max([w[1] for w in most_common])))
	for i,word_info in enumerate(most_common):
		word, occur = word_info
		print "{0:<3} |{1:<{col1}}|{2:<{col2}}".format(i,word,occur,col1=w_col1,col2=w_col2)


if __name__ == "__main__":
	top50_nostop(brown.words())

