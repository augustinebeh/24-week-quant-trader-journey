# 1. A list of 5 stock symbols you know
stocks_list = ["INTC", "OPEN", "NVDA", "PLUG", "ONDS"]

# 2. A list of their current prices (use any numbers)
stocks_price = [33.45, 7.89, 246.30, 23.56, 12.78]

# 3. A list of how many shares you "own" of each
shares_owned = [100, 200, 50, 150, 300]

# 4. Print the first stock, its price, and shares owned
print(f"Stock Symbol: {stocks_list[0]}")
print(f"Current Price: {stocks_price[0]}")
print(f"Shares owned: {shares_owned[0]}")

# 5. Printing the total number of stocks in my portfolio
total_stocks = len(stocks_list)
print(f"Total number of stocks: {total_stocks}")

# 6. Adding a new stock to the portfolio
stocks_list.append("APLD")
 
# 7. Printing the last stock in my portfolio
print(f"The last stock in my portfolio is: {stocks_list[-1]}")

# Printing end of list_practice.py
print("\n-- End of list_practice.py --\n")

