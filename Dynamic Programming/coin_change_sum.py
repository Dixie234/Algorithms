from typing import List

#all possible coin combinations to make an amount
def coinChangeSum(coins: List[int], amount: int) -> int:
    n = len(coins)
    dp_amounts = {}
    def coin_count(coins, n, amount):
        if (n, amount) in dp_amounts:
            return dp_amounts[(n, amount)]
        if amount == 0:
            return 1
        if amount < 0 or n == 0:
            return 0
        
        temp_1 = coin_count(coins, n, amount - coins[n-1])
        dp_amounts[(n, amount - coins[n-1])] = temp_1
        temp_2 = coin_count(coins, n-1, amount)
        dp_amounts[(n-1, amount)] = temp_2

        return temp_1 + temp_2
    
    return coin_count(coins, n, amount)

coins = [1,2,5]
sum = 5
print(coinChangeSum(coins, sum))
    