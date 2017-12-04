import os
from collections import Counter

def checkPhraseForAnagram(phrase):
	words = phrase.split(" ")				
	for i, word1 in enumerate(words):
		for j, word2 in enumerate(words):
			if i!=j and Counter(word1) == Counter(word2):
				return True
	return False
				
def Input():
	"Open input file of corresponding day."
	with open('{}.txt'.format(os.path.splitext(os.path.basename(__file__))[0]), 'r') as myfile:
		data=myfile.read()
	return data

#Day 4: Passphrases
phrases = Input().split("\n");
invalidPhrases = 0
for phrase in phrases:
	if checkPhraseForAnagram(phrase):
		invalidPhrases = invalidPhrases+1		
print "Valid phrases: " + str(len(phrases)-invalidPhrases)
