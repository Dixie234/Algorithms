def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    word_list = sentence.split(" ")
    for i, word in enumerate(word_list):
        if word.startswith(searchWord):
            return i + 1
    return -1