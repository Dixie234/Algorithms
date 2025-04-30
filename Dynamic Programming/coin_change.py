from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    def coin_change(coins, i, amount):
        if amount == 0:
            return 0
        if amount < 0 or i == len(coins):
            return float("inf")
        
        take = float("inf")
        if coins[i] > 0:
            take = coin_change(coins, i, amount - coins[i])
            if take != float("inf"):
                take += 1
        not_take = coin_change(coins, i+1, amount)
        return min(take, not_take)
    return coin_change(coins, 0, amount)