from typing import List


def change(amount: int, coins: List[int]) -> int:
    n = len(coins)
    dp = {}
    def change_recur(coins, n, amount):
        if (n, amount) in dp:
            return dp[(n, amount)]
        if amount == 0:
            return 1
        if amount < 0 or n == 0:
            return 0

        temp_1 = change_recur(coins, n, amount - coins[n-1])
        dp[(n, amount - coins[n-1])] = temp_1
        temp_2 = change_recur(coins, n-1, amount)
        dp[(n-1, amount)] = temp_2
        return temp_1 + temp_2
    return change_recur(coins, n, amount)