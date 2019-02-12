""" solution for Decode the Morse code challenge
convert Morse code to readable message"""

def singleMorse(m_code):
    return m_code.replace(m_code, MORSE_CODE[m_code])
    
def decodeMorse(morse_code):
    decodedMorse = []
    for word in morse_code.split('  '):
        decodedWord = []
        for m in word.split():
            decodedWord.append(singleMorse(m))
        decodedMorse.append(''.join(decodedWord))
    return ' '.join(decodedMorse).strip()