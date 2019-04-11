""" solution for Dubstep challenge
remove WUB from string to decode"""

def song_decoder(song):
    no_wub = song.split('WUB')
    no_empty = list(filter(None, no_wub))
    decode = " ".join(no_empty)
    return decode