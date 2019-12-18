""" solution Sudoku Solution Validator challenge
verify if the given answer of 9x9 sudoku is correct or not"""

def validSolution(board):
    # check vertical
    flip_board = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    for i in range(9):
        for j in range(9):
            flip_board[j][i] = board[i][j] 
    
    # check 3x3 boxes
    wait_list = []
    box_board = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    for n in range(1,10,3):
        count = 1
        for i in range(9):
            for j in range(count*n-1,count*n+2):
                wait_list.append(board[i][j])
                count += 1
            count = 1
    wait_list_count = 0
    for i in range(9):
        for j in range(9):
            box_board[i][j] = wait_list[wait_list_count]
            wait_list_count += 1

    return list_check(board) and list_check(flip_board) and list_check(box_board)

def list_check(input_lists):
    for i in input_lists:
        if sum(i) != 45:
            return False
    return True






# test
test1 = [[5, 3, 4, 6, 7, 8, 9, 1, 2],[6, 7, 2, 1, 9, 5, 3, 4, 8],[1, 9, 8, 3, 4, 2, 5, 6, 7],  [8, 5, 9, 7, 6, 1, 4, 2, 3],  [4, 2, 6, 8, 5, 3, 7, 9, 1],  [7, 1, 3, 9, 2, 4, 8, 5, 6],  [9, 6, 1, 5, 3, 7, 2, 8, 4],  [2, 8, 7, 4, 1, 9, 6, 3, 5],  [3, 4, 5, 2, 8, 6, 1, 7, 9]]
print(validSolution(test1))
