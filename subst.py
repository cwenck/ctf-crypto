#!/usr/bin/python

import base64

# input = "uozdovhhob zigrxfozgrmt slmvbyzwtvi"
input = "JedmRUT0sYMyReNlQOpdAYFqwPT0t2vqQPTgRPAyv2znAZvnueldRUTzvUTKsPRdueBztekyLYXat3BzvY9qsONrDaTPsYX0AYzzuqTrsYMyQeNdtaTcvOBaROIyQPE/"

# Range of 97 - 122
def getLetterWithOffset(offset, letter):
	letterNum = ord(letter)
	if letterNum <= ord('z') and letterNum >= ord('a'):
		letterNum += offset
		while letterNum > ord('z'):
			letterNum -= 26
		return chr(letterNum)
	elif letterNum <= ord('Z') and letterNum >= ord('A'):
		letterNum += offset
		while letterNum > ord('Z'):
			letterNum -= 26
		return chr(letterNum)
	else:
		return letter



def wordWithOffset(offset, word):
	out = ''
	for char in input:
		out += getLetterWithOffset(offset, char)
	return out

def reverseWordWithOffset(offset, word):
	return wordWithOffset(offset, word)[::-1]

def calcRotations():
	out = []
	for offset in range(0,26):
		out.append(wordWithOffset(offset, input))
	return out;

def b64DecodeRotations():
	rotations = calcRotations()
	decoded = []
	for rotation in rotations:
		decoded.append(normalCharsOnly(base64.b64decode(rotation), ' '))

	return decoded

def normalCharsOnly(text, unknownChar):
	output = ''
	for c in text:
		char_num = ord(c)
		if char_num >= 32 and char_num <= 126:
			output += c
		else:
			output += unknownChar
	return output

def matchesTrigram(text, trigram):
	if len(text) != 3 or len(trigram) != 3:
		return False

	trigram = trigram.lower()
	text = text.lower()

	remainingSpaces = 0
	index = 0
	for c in text:
		if c == ' ' and remainingSpaces > 0:
			remainingSpaces -= 1;
		elif c != trigram[index]:
			return False
		index += 1
	return True

def matchTrigramsInText(text):
	trigrams = [
	'the', 'and', 'tha', 'ent',
	'ing', 'ion', 'tio', 'for',
	'nde', 'has', 'nce', 'edt',
	'tis', 'oft', 'sth', 'men'
	]

	trigramCount = 1

	for i in range(0, len(text) - 2):
		threeCharText = text[i:i+3]
		for trigram in trigrams:
			if matchesTrigram(threeCharText, trigram):
				trigramCount += 1
	return trigramCount

def matchesBigram(text, bigram):
	if len(text) != 2 or len(bigram) != 2:
		return False

	bigram = bigram.lower()
	text = text.lower()
	return bigram == text


def matchBigramsInText(text):
	bigrams = [
	'th','he','in','er','an',
	're','nd','on','en','at',
	'ou','ed','ha','to','or',
	'it','is','hi','es','ng'
	]

	bigramCount = 0

	for i in range(0, len(text) - 1):
		twoCharText = text[i:i+2]
		for bigram in bigrams:
			if matchesBigram(twoCharText, bigram):
				bigramCount += 1
	return bigramCount

def englishRank(text):
	return float((matchBigramsInText(text) + matchTrigramsInText(text))) / float(len(text))

def printRotations():
	rotations = calcRotations()
	offset = 0
	for rotation in rotations:
		print(str(offset) + ': ' + rotation)
		offset += 1

def printDecodedRotations():
	decoded = b64DecodeRotations()
	offset = 0
	for line in decoded:
		print(str(englishRank(line)) + ' - ' + str(offset) + ': ' + str(line))
		offset += 1

def sortByEnglishRank(array):
	def keyFunc(line):
		return -englishRank(line)
	return sorted(array, key=keyFunc)
	# dictionary = {}
	# ranks = []
	# for line in array:
	# 	rank = englishRank(line)
	# 	dictionary[line] = rank
	# 	ranks.append(rank)

def printArray(array):
	for line in array:
		print(line)

printArray(sortByEnglishRank(b64DecodeRotations()))
# printArray(sortByEnglishRank([
# 	'flawlessly articulating honeybadger',
# 	'flawlessly articulating doneypazger',
# 	'flawlessly articulating doneymaqger',
# 	'flawlessly articulating moneypazger',
# 	'flawlessly articulating doneymazger',
# 	'flawlessly articulating doneymavger',
# 	'flawlessly articulating honeypazger',
# 	'flawlessly articulating moneybadger',
# 	'flawlessly articulating doneymahger',
# 	'flawlessly articulating honeymaqger',
# 	'flawlessly articulating doneypaxger'
# 	]))

# print(matchesBigram('te', 'tee'))
# printDecodedRotations()

