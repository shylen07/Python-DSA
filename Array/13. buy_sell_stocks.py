# Question: Find the maximum profit by buying and selling stocks.
# Created by Devender Singh

def max_profit(prices):
    max_profit = 0
    min_price = float('inf')
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit

# Driver code
prices = [7, 1, 5, 3, 6, 4]
print("Max profit:", max_profit(prices))
