# **1. Data Structure:**
# - Create a list called `portfolio`
# - Each item is a dictionary with: symbol, buying_price, current_price, shares
# - Include at least 3 different stocks

portfolio = []

tesla = {
    "symbol": "TSLA",
    "buying_price": 400.00,
    "current_price": 435.80,
    "shares": 100
}

nvidia = {
   "symbol": "NVDA",
   "buying_price": 155.00,
   "current_price": 184.93,
   "shares": 50
}

kenvue = {
   "symbol": "KVUE",
   "buying_price": 11.20,
   "current_price": 16.83,
   "shares": 350
}
portfolio = [tesla, nvidia, kenvue]

def calculate_stock_profit(buying_price, current_price, shares):
   investment = buying_price * shares
   current_value = current_price * shares
   current_profit = current_value - investment
   is_profitable = current_profit > 0
   profit_percentage = (current_profit / investment) * 100 if investment != 0 else 0
   return {
      "investment": investment,
      "current_value": current_value,
      "current_profit": current_profit,
      "profit_percentage": profit_percentage,
      "is_profitable": is_profitable
   }
# **2. For Each Stock, Calculate and Display:**
   # - Total cost (buying_price × shares)
   # - Current value (current_price × shares)
   # - Profit/Loss (current_value - investment)
   # - Profit percentage
   # - Whether it's profitable (✅) or not (❌)
for stock in portfolio:
   stock.update(calculate_stock_profit(stock["buying_price"], stock["current_price"], stock["shares"]))
   # stock["investment"] = stock["buying_price"] * stock["shares"]
   # stock["current_value"] = stock["current_price"] * stock["shares"]
   # stock["current_profit"] = stock["current_value"] - stock["investment"]
   # stock["profit_percentage"] = stock["current_profit"] / stock["investment"] * 100
   # stock["is_profitable"] = stock["current_profit"] >= 0


# print("\n============================================================")
# print("PORTFOLIO SUMMARY")
# print("============================================================")
print("\n============================================================")
print("STOCK DETAILS")
print("============================================================")
for stock in portfolio:
   for key, value in stock.items():
      if key == "buying_price" or key == "current_price" or key == "investment" or key == "current_value" or key == "current_profit":
         print(f"{key}: ${value:.2f}")
      elif key == "profit_percentage":
         print(f"{key}: {value:.2f}%")
      else: print(f"{key}: {value}")
   print("\n")
 

# **3. Portfolio Summary:**
# - Total amount invested across all stocks
# - Current total portfolio value
# - Overall profit/loss
# - Overall profit percentage

def calculate_portfolio_summary(portfolio):
   portfolio_invested = 0
   portfolio_value = 0
   portfolio_current_profit = 0
   portfolio_profit_percentage = 0





   for stock in portfolio:
      for key, value in stock.items():
         if key == "investment":
            portfolio_invested += value
         if key == "current_value":
            portfolio_value += value
         if key == "current_profit":
            portfolio_current_profit += value
   portfolio_profit_percentage = (portfolio_current_profit / portfolio_invested * 100) if portfolio_invested != 0 else 0
   return {
      "total_invested": portfolio_invested,
      "portfolio_value": portfolio_value,
      "overall_profit": portfolio_current_profit,
      "overall_profit_percentage": portfolio_profit_percentage
   }

portfolio_summary = calculate_portfolio_summary(portfolio)


print("============================================================")
print("PORTFOLIO SUMMARY")
print("============================================================")
print(f"Total Invested across all stocks:     ${portfolio_summary['total_invested']:.2f}")
print(f"Current total portfolio value:        ${portfolio_summary['portfolio_value']:.2f}")
print(f"Overall profit/loss:                  ${portfolio_summary['overall_profit']:.2f}")
print(f"Overall profit percentage:            {portfolio_summary['overall_profit_percentage']:.2f}%")
print("============================================================\n")


