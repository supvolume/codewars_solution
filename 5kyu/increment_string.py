""" solution for String incrementer challenge
increase the number at the end of the given string"""

def increment_string(strng):
    input_list = list(strng)
    digit_index_start = len(input_list)
    for i in range(len(input_list)-1,-1,-1):
        if input_list[i].isdigit() == False:
            break
        digit_index_start = i
        
    str_list = input_list[:digit_index_start]
    digit_list = input_list[digit_index_start:]
     
    if len(digit_list) == 0:
        input_list.append("1")
        return "".join(input_list)
    else:
        digit_len = len(digit_list)
        end_num = int("".join(digit_list))+1
        str_list.append(str(end_num).zfill(digit_len))
        return "".join(str_list)
