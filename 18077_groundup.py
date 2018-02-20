# Python script completely build from ground up:

fname = '18077_test.txt'

num_words = 0

# word to search for in tx
word_to_search = input("Word to search for: ")

# list of words 
wordlist = []
counter = []

i = 0

# find words in text
with open(fname) as f:
	for line in f:
		words = line.split()
		i += 1
		for wordsl in words:
			if wordsl == word_to_search:
				wordlist.append(word_to_search)
				print("word found in line %i" %i)
				counter.append(i)
			# else:
			# 	print("not found")
		num_words += len(words)
print("Number of words in %s" %fname)
print(num_words)
print(wordlist)
print(counter)
print("No of hits for word: %s" %word_to_search)
print(len(wordlist))






# import re #import regular expressions module

# #load kafka extract 
# data = open('kafka.txt', 'r').read

# # filetype?
# print(type(data()))

# # print amount of words
# wcount = re.findall('\w+', data())

# # print amount of words
# print(wcount)
