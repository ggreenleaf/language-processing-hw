# Write a program to create a table of word frequencies by genre, like the one given in Section 2.1 for modals. Choose your own words and try to find words whose presence (or absence) is typical of a genre. Discuss your findings
import nltk
from nltk.corpus import brown

cfd = nltk.ConditionalFreqDist(
	(genre,word.lower())
	for genre in brown.categories()
	for word in brown.words(categories=genre))


genres = ["news","religion","hobbies","science_fiction","romance","humor"]
words = ["who","what","when","where","why","which", "how"]

cfd.tabulate(conditions=genres,samples=words)