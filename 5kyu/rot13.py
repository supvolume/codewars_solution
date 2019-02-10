""" solution for Rot13 challenge
replaces a letter with the letter 13 letters after it in the alphabet"""

from codecs import encode as _dont_use_this_

def rot13(message):
    rotMessage = ''
    for m in message:
        if (ord(m) >= 65 and ord(m) <= 77) or (ord(m) >= 97 and ord(m) <= 109):
            rotMessage+=chr(ord(m)+13)
        elif (ord(m) > 77 and ord(m) <= 90) or (ord(m) > 109 and ord(m) <= 122):
            rotMessage+=chr(ord(m)-13)
        else:
            rotMessage+=m
    return rotMessage