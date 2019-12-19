""" solution for strip comment challenge
for each line, remove comment behind the markers
then remove the white space behind each line"""

def solution(string,markers):
    str_list = string.split("\n")
    no_marker = []
    for i in range(len(str_list)):
        marker_in_str = True
        for j in range(len(str_list[i])):
            if str_list[i][j] in markers:
                no_marker.append(str_list[i][:j].strip())
                marker_in_str = False
                break
        if marker_in_str:
            no_marker.append(str_list[i].strip())
    return "\n".join(no_marker)


# test
def main():
    print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))

if __name__ == "__main__":
    main()
