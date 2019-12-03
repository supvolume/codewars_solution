""" solution for Your order, please challenge
return string that order by the number contain in words
"""

def order(sentence):
    sen_list = sentence.split()
    n = len(sen_list)
    order_list = [''] * n
    for i in range(n):
        for j in sen_list:
            if str(i+1) in j:
                order_list[i] = j
    return ' '.join(order_list)

print(order("is2 Thi1s T4est 3a"))
