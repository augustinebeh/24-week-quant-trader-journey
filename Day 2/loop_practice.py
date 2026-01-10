# 1. Use your lists from Exercise 1
from list_practice import stocks_list, stocks_price, shares_owned

# 2. Loop through and print each stock symbol
print("-- Printing each stock symbol--")
for stock in stocks_list:
   print(f"{stock}")

# 3. Loop through symbols and prices together, showing both
print("\n-- Looping through symbols and prices together --")
for symbol, price in zip(stocks_list, stocks_price):
   print(f"Symbol: {symbol}")
   print(f"Price: {price}\n")

# 4. Calculate the total value of each stock (price × shares) using a loop
total_value = []
# Printing each stock, its price, shares owned, and total value
print("\n-- Looping through symbols, its price, shares owned, and total value --")
for symbol, price, shares in zip(stocks_list, stocks_price, shares_owned):
   value = round(price * shares, 2)
   total_value.append(value)

   print(f"Symbol: {symbol}")
   print(f"Price: ${price:.2f}")
   print(f"Shares owned: {shares}")
   print(f"Total Value: ${value:.2f}\n")


# 5. Calculate and print your total portfolio value (sum of all stock values)
portfolio_value = sum(total_value)
print(f"Total Portfolio Value: ${portfolio_value:.2f}")
