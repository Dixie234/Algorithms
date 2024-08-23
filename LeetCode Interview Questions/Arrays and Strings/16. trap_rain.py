from typing import List


def trap(height: List[int]) -> int:
    result = 0
    max_height = 0
    max_index = 0
    possible_trap = 0
    start_counting = False
    #left parse
    for i, column_height in enumerate(height):
        if start_counting:
            if column_height >= max_height:
                max_height = column_height
                result += possible_trap
                max_index = i
                possible_trap = 0
            else:
                possible_trap += max_height - column_height
        else:
            if column_height < max_height:
                start_counting = True
                possible_trap += max_height - column_height
            else:
                max_height = column_height

    #right parse
    possible_trap = 0
    start_counting = False
    max_height = 0
    sub_section = []
    if max_index == 0:
        sub_section = height[::-1]
    else:
        sub_section = height[:max_index - 1:-1]

    for column_height in sub_section:
        if start_counting:
            if column_height >= max_height:
                max_height = column_height
                result += possible_trap
                max_index = i
                possible_trap = 0
            else:
                possible_trap += max_height - column_height
        else:
            if column_height < max_height:
                start_counting = True
                possible_trap += max_height - column_height
            else:
                max_height = column_height    

    return result