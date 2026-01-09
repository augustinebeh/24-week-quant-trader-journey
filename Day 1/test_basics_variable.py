import os
from basic_variable import calculate_trading_metrics

def test_profit_calculation():
    # Test a profitable trade
    result = calculate_trading_metrics(100, 110, 10)
    assert result["total_investment"] == 1000
    assert result["current_profit"] == 100
    assert result["profit_percentage"] == 10.0
    assert result["is_profitable"] is True
    print("✅ Profit test passed")

def test_loss_calculation():
    # Test a losing trade
    result = calculate_trading_metrics(100, 90, 10)
    assert result["current_profit"] == -100
    assert result["is_profitable"] is False
    print("✅ Loss test passed")

def test_break_even():
    # Test zero profit
    result = calculate_trading_metrics(100, 100, 5)
    assert result["current_profit"] == 0
    assert result["is_profitable"] is False
    print("✅ Break-even test passed")

if __name__ == "__main__":
    print("\nRunning tests...")

    tests = [
        ("Profit Calculation", test_profit_calculation),
        ("Loss Calculation", test_loss_calculation),
        ("Break-even", test_break_even),
    ]

    all_passed = True
    for name, test_func in tests:
        try:
            test_func()
        except AssertionError as e:
            print(f"❌ {name} failed")
            all_passed = False
# Pause using system command
        os.system("sleep 0.5")
        # Note: time.sleep(0.2) is the standard Pythonic way
    if all_passed:
        print("\nAll tests passed successfully!")
    else:
        print("\nSome tests failed.")
