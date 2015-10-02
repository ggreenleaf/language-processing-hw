import simple_nlp as nlp

with open("books/The Time Machine.txt") as f:
	frankenstein = f.read()
with open("books/Frankenstein.txt") as f:
	time_machine = f.read()



#generating bigram sentences for The Time Machine
def generate_bigram_text(text):
	words = nlp.mark_sents(nlp.words(text))
	bigrams = nlp.bigrams(words)
	fd = nlp.freq_dist(bigrams)
	# for i in xrange(25):
	# 	sentence = nlp.generate_sent(fd)
	return [nlp.generate_sent(fd) for i in xrange(25)]

def generate_trigram_text(text):
	pass


if __name__ == "__main__":
	with open("my sents.txt","w") as f:
		f.write("Frankenstein sentences from bigrams\n\n")
		f.write("\n".join(generate_bigram_text(frankenstein)))
		f.write("\n\nTime Machine sentences from bigrams\n\n")
		f.write("\n".join(generate_bigram_text(time_machine)))
		f.write("\n\nCombined Frankenstein and Time Machine bigram\n\n")
		f.write("\n".join(generate_bigram_text(time_machine + frankenstein)))





