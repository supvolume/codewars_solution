""" solution for Create Phone Number challenge
create phone number with given pattern from a list of number"""

def create_phone_number(n):
    str_list = list(map(str,n))
    number_str = ''.join(str_list)
    return '(' + number_str[:3] + ') ' + number_str[3:6] + '-' + number_str[6:]


# test
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
