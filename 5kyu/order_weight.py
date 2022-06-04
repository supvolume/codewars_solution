""" solution for Weight for weight challenge
sort number (weight) by the sum of number
https://www.codewars.com/kata/55c6126177c9441a570000cc/python"""


def order_weight(strng):
    weight_dict = {}    # to record weight of weight as value
    weight_list = strng.split(" ")
    weight_list = sorted(weight_list)   # string sort in case the weight of weight are the same
    for weight in weight_list:
        if weight != " ":
            number_w = 0
            for n in weight:
                number_w += int(n)
            if weight not in weight_dict:
                    weight_dict[weight] = [number_w, 1]
            else:
                weight_dict[weight][1] += 1
    # sort dict by value
    weight_dict = {k: v for k, v in sorted(weight_dict.items(), key=lambda item: item[1][0])}

    output_list = []
    for k, v in weight_dict.items():
        for i in range(v[1]):
            output_list.append(k)
    return " ".join(output_list)
            
    


if __name__ == "__main__":
    print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))
