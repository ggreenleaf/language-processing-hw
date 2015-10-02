import simple_nlp as nlp

with open("books/Aether and Gravitation.txt") as f:
	aether = f.read()

with open("books/Frankenstein.txt") as f:
	frankenstein = f.read()



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
	with open("my sents.txt","a") as f:
		f.write("{title} sentences based of {model} language model\n\n".format(title=title,model=model))
		for i, sent in sents:
			f.write("{i}. {sent}\n".format(i=i,sent=sent))

	   


if __name__ == "__main__":
	#Aether bigrams
	sents = enumerate(generate_bigram_text(aether))
	write_file("Aether and Gravitation","bigram",sents)
	#Aether trigrams
	sents = enumerate(generate_trigram_text(aether))
	write_file("Aether and Gravitation","trigram",sents)
	#Frankenstein bigrams
	sents = enumerate(generate_bigram_text(frankenstein))
	write_file("Frankenstein","bigram",sents)
	#Frankenstein trigrams
	sents = enumerate(generate_trigram_text(frankenstein))
	write_file("Frankenstein","trigram",sents)
	#combined bigrams
	sents = enumerate(generate_bigram_text(aether+frankenstein))
	write_file("Aether and Gravitation with Frankenstein","bigram",sents)
	#combined trigrames
	sents = enumerate(generate_trigram_text(aether+frankenstein))
	write_file("Aether and Gravitation with Frankenstein","trigram",sents)







