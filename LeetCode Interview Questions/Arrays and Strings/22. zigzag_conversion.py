import itertools


def convert(s: str, numRows: int) -> str:
    if(numRows  < 2):
        return s
    row_start = 1
    going_down = True
    mapping = {}
    for char in s:
        if not row_start in mapping:
            mapping[row_start] = char
        else:
            mapping[row_start] += char

        if going_down and row_start == numRows:
            going_down = False  
        elif not going_down and row_start == 1:
            going_down = True   

        if going_down:
            row_start += 1
        else:
            row_start -= 1
    return ''.join(mapping.values())

        
s = "PAYPALISHIRING"
numRows = 3

result = convert(s, numRows)
print(result)