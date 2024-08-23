from typing import List

def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    min_price = prices[0]
    prev_price = prices[0]
    increasing = True
    for price in prices[1:]:
        if price < prev_price:
            if increasing:
                max_profit += prev_price - min_price
            min_price = price
            increasing = False
        elif price > prev_price:
            increasing = True      
        prev_price = price

    if prev_price > min_price and increasing:
        max_profit += prev_price - min_price
        
    return max_profit




prices = [7,1,5,3,6,4]
prices = [1,2,3,4,5]
prices = [5,2,3,2,6,6,2,9,1,0,7,4,5,0]
#1, 4, 7, 7, 1
profit = maxProfit(prices)
print(profit)
