import simple_nlp as nlp
from sys import argv




#generating bigram sentences for The Time Machine
def generate_bigram_text(text):
	words = nlp.mark_sents(nlp.words(text))
	bigrams = nlp.bigrams(words)
	fd = nlp.freq_dist(bigrams)
	return [nlp.generate_sent(fd) for i in xrange(25)]

def generate_trigram_text(text):
	words = nlp.mark_sents(nlp.words(text))
	trigrams = nlp.trigrams(words)
	fd = nlp.freq_dist(trigrams)
	return [nlp.generate_sent(fd) for i in xrange(25)]

def write_file(title,model,sents):
	'''title text model is based from
	   ngram model to write
	   list of sentences to write to file'''
	sentfile = argv[3]
	with open(sentfile,"a") as f:
		f.write("\n\n{title} sentences based off {model} language model\n\n".format(title=title,model=model))
		for i, sent in sents:
			f.write("{i}. {sent}\n".format(i=i,sent=sent))

	   


if __name__ == "__main__":
	book1 = argv[1]
	book2 = argv[2]
	with open(book1) as f:
		text1 = f.read()

	with open(book2) as f:
		text2 = f.read()

	#text1 bigrams
	sents = enumerate(generate_bigram_text(text1))
	write_file("text1","bigram",sents)
	#text1 trigrams
	sents = enumerate(generate_trigram_text(text1))
	write_file("text1","trigram",sents)
	#text2 bigrams
	sents = enumerate(generate_bigram_text(text2))
	write_file("text2","bigram",sents)
	#text2 trigrams
	sents = enumerate(generate_trigram_text(text2))
	write_file("text2","trigram",sents)
	#combined bigrams
	sents = enumerate(generate_bigram_text(text1+text2))
	write_file("text1 and text2","bigram",sents)
	#combined trigrames
	sents = enumerate(generate_trigram_text(text1+text2))
	write_file("text1 and text2","trigram",sents)







