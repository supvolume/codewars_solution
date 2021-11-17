"""solution for Replace With Alphabet Position challenge"""

def alphabet_position(text):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    return_list = []
    for i in text:
        find_alpha = alpha.find(str(i).lower())
        if find_alpha != -1:
            return_list.append(str(find_alpha+1))
    return " ".join(return_list)


# test
print(alphabet_position("The sunset sets at twelve o' clock."))
