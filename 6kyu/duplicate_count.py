""" solution for Counting Duplicates
return the number of characters that have duplicates"""

def duplicate_count(text):
    text = text.lower()
    count_text = {}
    count_dup = 0
    for i in text:
        if i not in count_text:
            count_text[i] = 1
        else:
            count_text[i] += 1
    for j in count_text:
        if count_text[j] > 1:
            count_dup += 1
    return count_dup
