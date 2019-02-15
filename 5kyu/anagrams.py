""" solution for Where my anagrams at? challenge
check if word in array is an annagram of word in first arg"""

def anagrams(word, words):
    anagrams = []
    for w in words:
        if len(w) == len(word) and set(w) == set(word):
            anagrams.append(w)
    return anagrams