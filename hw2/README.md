<h1>Homework Description</h1>

Select two different ebooks of your choosing from Project Gutenberg:
http://www.gutenberg.org/

Tokenize the text of both books into sentences. Add additional special tokens for sentence start and end (<s> and </s> are commom). These extra tokens should be considered as words in your n-gram language model.

Create six different language models, both a bigram (2-gram) and trigram (3-gram) model—i.e. two from each of the two books plus two from a hybrid created from the two books combined.

Generate six random texts of 25 sentences each. Each text should be generated from one each of the six language models.

You may choose any programming language for this task.

Submit the following:
A one page report including a description of your approach, language, 3rd party libraries, etc.
The text of your two chosen books
All your source code with a brief description of how to build and compile.
The contents of your six generated text examples
All elements should be archived into a single file.


<h1>Running Program</h1>

First you need to have python installed on your system. 

you can run the program from the command line by running the following command

python main.py book1Path book2Path sentFile

where book1Path is the path to the first text and book2Path is the path to the second text

The last argument is the file name you want to save the generated sentences to.

