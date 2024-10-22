from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    if not prerequisites:
        return True
    
    preq_set = { (course[0], course[1]) for course in prerequisites }
    reversed_tuple_list = [(course[1], course[0]) for course in prerequisites]
    for combo in reversed_tuple_list:
        if combo in preq_set:
            return False
    return True