from collections import Counter
from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    #validate columns
    for i in range(9):
        vals = set()
        for j in range(9):
            val = board[i][j] 
            if val in vals:
                return False
            elif val != '.':
                vals.add(val)

    #validate rows
    for i in range(9):
        vals = set()
        for j in range(9):
            val = board[j][i] 
            if val in vals:
                return False
            elif val != '.':
                vals.add(val)
                
    #validate sections
    prev_i = 0
    prev_j = 0
    for i in range(2, len(board), 3):
        prev_j = 0
        for j in range(2, len(board), 3):
            vals = set()
            for k in range(prev_i, i + 1):
                for l in range(prev_j, j + 1):
                    val = board[k][l]
                    if val in vals:
                        return False
                    elif val != '.':
                        vals.add(val)
            prev_j = j + 1
        prev_i = i + 1

    return True

def validate_columns(board:List[List[str]]) -> bool:
    for i in range(9):
        vals = set()
        for j in range(9):
            val = board[i][j] 
            if val in vals:
                return False
            elif val != '.':
                vals.add(val)
    return True

def validate_rows(board:List[List[str]]) -> bool:
    for i in range(9):
        vals = set()
        for j in range(9):
            val = board[j][i] 
            if val in vals:
                return False
            elif val != '.':
                vals.add(val)
    return True

def validate_sections(board:List[List[str]]) -> bool:
    prev_i = 0
    prev_j = 0
    for i in range(2, len(board), 3):
        prev_j = 0
        for j in range(2, len(board), 3):
            vals = set()
            for k in range(prev_i, i + 1):
                for l in range(prev_j, j + 1):
                    val = board[k][l]
                    if val in vals:
                        return False
                    elif val != '.':
                        vals.add(val)
            prev_j = j + 1
        prev_i = i + 1
    return True

# board = [["5","3",".",".","7",".",".",".","."]
#         ,["6",".",".","1","9","5",".",".","."]
#         ,[".","9","8",".",".",".",".","6","."]
#         ,["8",".",".",".","6",".",".",".","3"]
#         ,["4",".",".","8",".","3",".",".","1"]
#         ,["7",".",".",".","2",".",".",".","6"]
#         ,[".","6",".",".",".",".","2","8","."]
#         ,[".",".",".","4","1","9",".",".","5"]
#         ,[".",".",".",".","8",".",".","7","9"]]
board = [[".",".",".",".","5",".",".","1","."]
        ,[".","4",".","3",".",".",".",".","."]
        ,[".",".",".",".",".","3",".",".","1"]
        ,["8",".",".",".",".",".",".","2","."]
        ,[".",".","2",".","7",".",".",".","."]
        ,[".","1","5",".",".",".",".",".","."]
        ,[".",".",".",".",".","2",".",".","."]
        ,[".","2",".","9",".",".",".",".","."]
        ,[".",".","4",".",".",".",".",".","."]]

result = isValidSudoku(board)
print(result)






