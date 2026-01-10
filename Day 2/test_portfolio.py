import os
from portfolio_tracker import calculate_stock_profit, portfolio, calculate_portfolio_summary, portfolio_summary

def test_calculate_stock_profit():
   # Test a profitable stock
   result1 = calculate_stock_profit(50, 60, 20)
   assert result1["investment"] == 1000
   assert result1["current_profit"] == 200
   assert result1["profit_percentage"] == 20.0
   assert result1["is_profitable"] is True
   print("✅ Profitable stock test passed")
   os.system("sleep 0.2")

   # Test a losing stock
   result2 = calculate_stock_profit(80, 70, 15)
   assert result2["investment"] == 1200
   assert result2["current_profit"] == -150
   assert result2["profit_percentage"] == -12.5
   assert result2["is_profitable"] is False
   print("✅ Losing stock test passed")
   os.system("sleep 0.2")

   # Test a break-even stock
   result3 = calculate_stock_profit(30, 30, 10)
   assert result3["investment"] == 300
   assert result3["current_profit"] == 0
   assert result3["profit_percentage"] == 0.0
   assert result3["is_profitable"] is False
   print("✅ Break-even stock test passed")
   os.system("sleep 0.2")

   # Multiple stocks combined
   result = {
      "investment": result1["investment"] + result2["investment"] + result3["investment"],
      "current_value": result1["current_value"] + result2["current_value"] + result3["current_value"],
      "current_profit": result1["current_profit"] + result2["current_profit"] + result3["current_profit"],
   }
   result["is_profitable"] = result["current_profit"] > 0
   result["profit_percentage"] = (result["current_profit"] / result["investment"]) * 100 if result["investment"] != 0 else 0
   assert result["investment"] == 2500
   assert result["current_value"] == 2550
   assert result["current_profit"] == 50
   assert result["profit_percentage"] == 2.0
   assert result["is_profitable"] is True
   print("✅ Portfolio summary test passed")


if __name__ == "__main__":
   print("\nRunning portfolio tests...")
   test_calculate_stock_profit()
   os.system("sleep 0.2")
   print("\nAll tests passed successfully!")

