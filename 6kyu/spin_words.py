""" solution for Stop gninnipS My sdroW! challenge
reverse word that have length more than or equal to 5"""

def spin_words(sentence):
    spin = ''
    for word in sentence.split():
        if len(word) > 4:
            spin = ' '.join([spin,word[::-1]])
        else:
            spin = ' '.join([spin,word])
    return spin.strip()