import copy
from typing import List


def gameOfLife(board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    row_length = len(board[0])
    column_length = len(board)
    new_board = copy.deepcopy(board)
    for i in range(column_length):
        for j in range(row_length):
            current_position = (i, j)
            position_value = board[i][j]
            available_positions = get_availble_positions(current_position, row_length, column_length)
            neibours = 0
            for position in available_positions:
                column, row = position
                neibours += board[column][row]
            if neibours < 2 or neibours > 3:
                new_board[i][j] = 0
            if position_value == 0 and neibours == 3:
                new_board[i][j] = 1

    for i in range(column_length):
        for j in range(row_length):
            board[i][j] = new_board[i][j]


position_adjustments = [(-1, -1), (0, -1), (1, -1),
                        (-1, 0), (1, 0),
                        (-1, 1), (0, 1), (1, 1)]

def get_availble_positions(current_position, row_length, column_length):
    lower_bound = 0
    available_positions = []
    for adjustment in position_adjustments:
        column, row = current_position
        adjust_column, adjust_row = adjustment
        adjusted_column, adjusted_row = column + adjust_column, row + adjust_row
        if (adjusted_column < column_length and adjusted_column >= lower_bound) and (adjusted_row < row_length and adjusted_row >= lower_bound):
            available_positions.append((adjusted_column, adjusted_row))
    return available_positions

board = [[0,1,0],
         [0,0,1],
         [1,1,1],
         [0,0,0]]
gameOfLife(board)
print(board)