stock = {
    'GOOG': 520.54,
    'FB': 76.45,
    'YHOO': 39.28,
    'AMZN': 306.21,
    'AAPL': 99.76
}

print(stock)

min_price = min(zip(stock.values(), stock.keys()))
max_price = max(zip(stock.values(), stock.keys()))

print(min_price)
print(max_price)

prices_sorted = sorted(zip(stock.values(), stock.keys()))
print(prices_sorted)