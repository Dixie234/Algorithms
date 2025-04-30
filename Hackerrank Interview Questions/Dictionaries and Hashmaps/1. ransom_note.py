from typing import Counter, List


def checkMagazine(magazine:List[str], note:List[str]):
    mag_map = Counter(magazine)
    for word in note:
        if word not in mag_map:
            print("No")
            return
        else:
            mag_map[word] -= 1
            if mag_map[word] == 0:
                del mag_map[word]
    print("Yes")