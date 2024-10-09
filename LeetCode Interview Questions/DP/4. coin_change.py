from typing import List

#recusion no memoization
def coinChange(coins: List[int], amount: int) -> int:
    total = amount
    num_coins = { 0: 0 }
    def coin_check(amount, coin_total=0):            
        for coin in coins:
            if (amount - coin) > 0:
                coin_check(amount - coin, coin_total + 1)
            elif (amount - coin) == 0:
                if total in num_coins:
                    num_coins[total] = min(num_coins[total], coin_total + 1)
                else:
                    num_coins[total] = coin_total + 1
    coin_check(amount)
    return num_coins[total] if amount in num_coins else -1

#bottom-up solution
def coinChange(coins: List[int], amount: int) -> int:
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[amount] if dp[amount] != amount + 1 else -1


# amount = 7
# coins = [3,4,5]
coins = [4,3,2]
amount = 11
result = coinChange(coins, amount)
print(result)
            