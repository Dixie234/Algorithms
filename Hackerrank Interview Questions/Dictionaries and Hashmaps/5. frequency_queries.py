from typing import List


def freqQuery(queries:List[tuple[int, int]]):
    store = {}
    freqs = {}
    results_3 = []
    for type, val in queries:
        if type == 1:
            if val in store:
                store[val] += 1
                if store[val] not in freqs:
                    freqs[store[val]] = 1
                    freqs[store[val] - 1] -= 1
                else:
                    freqs[store[val]] += 1
                    freqs[store[val] - 1] -= 1
            else:
                store[val] = 1
                if store[val] not in freqs:
                    freqs[store[val]] = 1
                else:
                    freqs[store[val]] += 1

        elif type == 2:
            if val in store:
                if store[val] > 1:
                    if freqs[store[val]] == 1:
                        del freqs[store[val]]
                    else:
                        freqs[store[val]] -= 1
                    store[val] -= 1
                else:
                    if freqs[store[val]] == 1:
                        del freqs[store[val]]
                    else:
                        freqs[store[val]] -= 1
                    del store[val]

        else:
            if val in freqs:
                results_3.append(1)
            else:
                results_3.append(0)
    return results_3


queries = [(1, 5),(1, 6),(3, 2),(1, 10),(1, 10),(1, 6),(2, 5),(3, 2)]
result = freqQuery(queries)