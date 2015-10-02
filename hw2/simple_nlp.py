from collections import defaultdict
from random import random 
def mark_sents(words):
	'''return words with <s>,</s> marking the start and 
	end of sentences. Each <s> is a word'''

	marked_words = ["<s>"] #list of words with sentence markers added as words
 	with open("abbrev.txt") as f:
		common_abbrev = f.read().split("\n")
    
    #Simple sentence parser
	#if period it ends a sentence	
	#if word is in common abbrevitions don't end sentence
	#assume all sentences either end in . ! ?     
	for word in words:
		if word.endswith((".","!","?")):
			if word not in common_abbrev:
				#add the word, the punctuation, and the end sentence marker to marked_words
				marked_words.extend([word[:-1],word[-1],"</s>","<s>"])
				continue	
		marked_words.append(word)

	return marked_words #get rid of null can clean up later

def words(text):
	text = text.replace("\r\n"," ")
	return text.replace("\xef\xbb\xbf","").lower().split()

def bigrams(words):
	return [(words[i-1],words[i]) for i in xrange(1,len(words))] 

def trigrams(words):
	return [(words[i-2],words[i-1],words[i]) for i in xrange(2,len(words))] 

def freq_dist(words):
	'''return a dictionary whose key is a word in words 
	and value is the number of occurences in words'''
	d = defaultdict(int)
	for w in words: d[w] += 1
	return d


def strip(words):
	'''strip markers from word list and fix basic grammar'''

	sentence = " ".join(word for word in filter(lambda x: x != "<s>" and x != "</s>", words))
	sentence = sentence[:-2] + sentence[-1:]
	return sentence.capitalize()

def generate_sent(fd):
	'''generate a sentence given a frequency distribution of words'''
	sentence = ["<s>"] #start of a sentence is always a <s>
	# while sentence[-1] != "</s>":
	while "</s>" not in sentence:
		cur_word = sentence[-1]
		table = get_prob_table(fd,cur_word)	#generate a new probability table for given current word										
		word_list = get_next_word(table) #get next word based on probability table
		# sentence.append(word)
		sentence.extend(word_list)

	return strip(sentence)

def get_next_word(prob_table):
	'''returns a list of words'''
	cur_total = 0
	p = random()
	for key, prob in sorted(prob_table.items(), key=lambda x: x[-1], reverse=True): #last element of items is the probability
		cur_total += prob
		if p < cur_total:
			return key[1:] #if using n grame we need to add the next 1-n words of the ngram

def get_prob_table(fd,word):
	prob_table = defaultdict(float)
	#sum of the total number of occurences of ngram whose 1st word is word
	total = sum([fd[key] for key in fd.keys() if key[0] == word]) 
	ngrams = [key for key in fd.keys() if key[0] == word] #list of keys whose first word is word
	
	for key in ngrams: 
		prob_table[key] = float(fd[key]) / total

	return prob_table



