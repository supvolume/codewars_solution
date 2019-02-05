""" solution for Highest Scoring Word challenge
 find word that has highest score
 where a = 1, b = 2, c = 3 etc """

def high(x):
	highScore=0
	words = x.split(' ')
	for w in words:
		score=0
		char = list(w)
		for c in char:
			score+=ord(c)-96
		if score > highScore:
			highScore=score
			highWord = w
	return highWord
