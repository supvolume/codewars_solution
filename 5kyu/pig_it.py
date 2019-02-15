""" solution for Simple Pig Latin challenge
Move the first letter of each word to the end of it, then add "ay" to the end of the word"""

def pig_it(text):
    latin = []
    for word in text.split():
        if word == '!' or word == '?':
            latin.append(word)
        else:
            new_word = ''.join([word[1:],word[0],'ay'])
            latin.append(new_word)
    return ' '.join(latin)