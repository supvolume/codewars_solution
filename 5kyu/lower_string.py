""" solution for First non-repeating character challenge
find first non-repeating character in string"""

def first_non_repeating_letter(string):
    lower_string = []
    for s in list(string):
        lower_string.append(s.lower())
    not_repeat = ''
    for c in list(string):
        if lower_string.count(c.lower()) == 1:
            not_repeat = c
            break
    return not_repeat