# Solutions for Disemvowel Trolls challenge

def disemvowel(string_):
    vowel = ['a', 'e', 'i', 'o', 'u']
    no_vowel = []
    
    for i in string_:
        if i.lower() not in vowel:
            no_vowel.append(i)
    return ''.join(no_vowel)



print(disemvowel("This website is for losers LOL!"))
