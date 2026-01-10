# 1. Create a dictionary for one stock with: symbol, buying_price, current_price, shares
stock = {
    "symbol": "TSLA",
    "buying_price": 400.00,
    "current_price": 435.80,
    "shares": 100
}

# 2. Print each key-value pair using a loop
for key, value in stock.items():
   print(f"{key}: {value}")

# 3. Calculate and add a "profit" key to the dictionary
stock["profit"] = round((stock["current_price"] - stock["buying_price"]) * stock["shares"], 2)
print("profit:",stock["profit"],"\n")

# 4. Update the current_price to a new value
stock["current_price"] = 494.44

# 5. Print the updated dictionary
for key, value in stock.items():
   stock["profit"] = round((stock["current_price"] - stock["buying_price"]) * stock["shares"], 2)
   print(f"{key}: {value}")
