from typing import List

# # = stone
# * = obstacle
# . = blank

# [#, *, #, ., ., ., #, *]
# [#, *, ., ., ., #, #, *]
def rotateTheBox(boxGrid: List[List[str]]) -> List[List[str]]:
    for row in boxGrid:
        for i in range(len(row) - 1, -1, -1):
            if row[i] == ".":
                compare_index = 1
                while i - compare_index >= 0:                 
                    if row[i - compare_index] == "*":
                        break
                    elif row[i - compare_index] == "#":
                        row[i] = "#"
                        row[i - 1] = "."
