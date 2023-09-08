def maxProfit(prices):
    max_profit = 0
    min_price = 9999
    for current_price in prices:
        if current_price < min_price:
            min_price = current_price
        todays_profit = current_price - min_price
        if todays_profit > max_profit:
            max_profit = todays_profit
    return max_profit


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]

    minimum_stock = maxProfit(prices)
    print(minimum_stock)