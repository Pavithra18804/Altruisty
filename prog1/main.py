def max_profit(prices):
    if not prices:
        return 0
    
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        # Update the minimum price so far
        min_price = min(min_price, price)
        # Calculate the profit if sold at current price
        profit = price - min_price
        # Update the maximum profit so far
        max_profit = max(max_profit, profit)
    
    return max_profit


n = 6
prices = [5, 10, 3, 9, 1, 8]
print(max_profit(prices))  

