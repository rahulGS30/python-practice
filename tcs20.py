def max_profit(prices):
    min_price = prices[0]
    max = 0
    for i in range(len(prices)):
        if i < min_price:
            min_price = i
        profit = i - min_price
        if profit>max:
            max=profit
    return profit
    



prices = [7,1,5,3,6,4]
print(max_profit(prices))