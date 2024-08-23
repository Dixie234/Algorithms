import math
from typing import List


def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    row_words = []
    row_words_length = 0
    width_left = maxWidth

    result = []
    for word in words:
        if len(word) > width_left:
            result.append(justify_row(row_words, row_words_length, maxWidth))
            row_words = [word]
            row_words_length = len(word)
            width_left = maxWidth - (len(word) + 1)
        else:
            row_words.append(word)
            row_words_length += len(word)
            width_left -= len(word) + 1
    if row_words_length != 0:
        result.append(justify_final_row(row_words, row_words_length, maxWidth))
    return result

def justify_row(words: List[str], words_string_length: int, maxWidth: int) -> str:
    num_spaces = maxWidth - words_string_length
    number_of_words = len(words)
    number_of_spaces_between_words = number_of_words - 1
    if number_of_words == 1:
        result = words[0] + (" " * num_spaces)
    else:
        spaces_list = [0] * number_of_spaces_between_words
        derive_spaces(spaces_list, number_of_spaces_between_words, num_spaces)
        result = create_string(words, spaces_list)
    
    return result

def derive_spaces(spaces_list: List[int], number_of_spaces_between_words: int, num_spaces: int) -> None:
    for i in range(len(spaces_list)):
        if num_spaces > number_of_spaces_between_words:
            spaces_list[i] = math.ceil(num_spaces / number_of_spaces_between_words)
        else: 
            spaces_list[i] = 1
        num_spaces -= spaces_list[i]
        number_of_spaces_between_words -= 1

def create_string(words: List[str], spaces_list: List[int]) -> str:
    result = ""
    for i in range(len(words) - 1):
        result += words[i] + (" " * spaces_list[i])
    result += words[len(words) - 1]
    return result

def justify_final_row(words: List[str], words_string_length: int, maxWidth: int) -> str:
    num_spaces = maxWidth - words_string_length
    number_of_words = len(words)
    result = ""
    if number_of_words == 1:
        result += words[0] + (" " * num_spaces)   
    else:
        for word in words:
            if num_spaces > 0:
                result += word + " "
                num_spaces -= 1
            else:
                result += word
        result += " " * num_spaces
    return result


result = fullJustify(["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"], 16)
print(result)
