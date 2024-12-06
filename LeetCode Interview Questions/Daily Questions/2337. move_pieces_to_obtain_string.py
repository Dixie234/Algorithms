from collections import Counter


def canChange(start: str, target: str) -> bool:
    start_counter = Counter(start)
    target_counter = Counter(target)

    if start_counter != target_counter:
        return False

    start_letter_order = start.replace("_", "")
    target_letter_order = target.replace("_", "")

    if start_letter_order != target_letter_order:
        return False
    
    start_indicies = {
        "L": [i for i, val in enumerate(start) if val == "L"],
        "R": [i for i, val in enumerate(start) if val == "R"]
    }
    target_indicies = {
        "L": [i for i, val in enumerate(target) if val == "L"],
        "R": [i for i, val in enumerate(target) if val == "R"]
    }

    for i in range(len(start_indicies["L"])):
        start_index = start_indicies["L"][i]
        target_index = target_indicies["L"][i]
        if start_index < target_index:
            return False
    
    for i in range(len(start_indicies["R"])):
        start_index = start_indicies["R"][i]
        target_index = target_indicies["R"][i]
        if start_index > target_index:
            return False     

    return True   

        