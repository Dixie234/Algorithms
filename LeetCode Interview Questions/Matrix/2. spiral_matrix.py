from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    result = []
    north_border = 0
    east_border = 0
    south_border = 0
    west_border = 0
    current_direction = "east"
    width = len(matrix[0]) - 1
    height = len(matrix) - 1
    can_move = True
    i = 0
    j = 0
    flattened_list = [item for row in matrix for item in row]
    list_length = len(flattened_list)
    while can_move:
        if list_length - len(result) == 1:
            result.append(matrix[i][j])
            can_move = False
            break
        if current_direction == "east":
            if j < width - east_border:
                result.append(matrix[i][j])
                j += 1
            else: 
                current_direction = "south"
                north_border += 1
        if current_direction == "south":
            if i < height - south_border:
                result.append(matrix[i][j])
                i += 1
            else:
                current_direction = "west"
                east_border += 1
        if current_direction == "west":
            if j > 0 + west_border:
                result.append(matrix[i][j])
                j -= 1
            else:
                current_direction = "north"
                south_border += 1
        if current_direction == "north":
            if i > 0 + north_border:
                result.append(matrix[i][j])
                i -= 1
            else: 
                current_direction = "east"
                west_border += 1
    return result


matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = spiralOrder(matrix)
print(result)
