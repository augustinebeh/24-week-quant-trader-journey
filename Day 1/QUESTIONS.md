# Day 1 Practice Questions

## 📝 Self-Assessment Questions

After completing Day 1, test your understanding with these questions. Try to answer them without looking back at your notes!

---

## Quick Check Questions

### 1. Data Types
**Q:** What data type would you use for a stock symbol?

<details>
<summary>Click to see answer</summary>

**A:** String (text)

Example: `stock_symbol = "AAPL"`
</details>

### 2. Operators
**Q:** What's the difference between `=` and `==`?

<details>
<summary>Click to see answer</summary>

**A:** 
- `=` is **assignment** - it stores a value in a variable
  - Example: `price = 150.25`
- `==` is **comparison** - it checks if two values are equal
  - Example: `if price == 150.25:`
</details>

### 3. Boolean Logic
**Q:** If you have `profit = 500` and `loss = 300`, what would `profit > loss` return?

<details>
<summary>Click to see answer</summary>

**A:** `True`

Because 500 is greater than 300, the comparison returns `True`.
</details>

---

## Concept Application Questions

### 4. F-String Formatting
**Q:** What does `:.2f` do in the f-string `f"Profit: ${profit:.2f}"`?

<details>
<summary>Click to see answer</summary>

**A:** It formats the float to show exactly 2 decimal places.

- `:` means "format this value"
- `.2` means "show 2 decimal places"
- `f` means "as a float (decimal number)"

Example: `{1080.123:.2f}` becomes `1080.12`
</details>

### 5. Boolean Shortcuts
**Q:** How can you simplify this code?
```python
if current_profit > 0:
    is_profitable = True
else:
    is_profitable = False
```

<details>
<summary>Click to see answer</summary>

**A:** Use the boolean shortcut:
```python
is_profitable = current_profit > 0
```

The comparison `current_profit > 0` directly returns `True` or `False`, which can be stored in the variable.
</details>

---

## Coding Challenges

### Challenge 1: Basic Stock Calculator
**Task:** Create variables for a stock and print them.

**Requirements:**
- Pick any stock symbol (string)
- Set a buying price (float)
- Set current market price (float)
- Set number of shares owned (integer)
- Print all values using f-strings

<details>
<summary>Click to see solution</summary>

```python
# Stock information
stock_symbol = "AAPL"
buying_price = 150.00
current_market_price = 165.50
shares_owned = 10

# Print results
print(f"Stock: {stock_symbol}")
print(f"Buying Price: ${buying_price:.2f}")
print(f"Current Price: ${current_market_price:.2f}")
print(f"Shares: {shares_owned}")
```
</details>

---

### Challenge 2: Calculate P&L
**Task:** Using the variables from Challenge 1, calculate:
- Total investment cost
- Current portfolio value
- Profit or loss
- Profit percentage
- Whether it's profitable (boolean)

<details>
<summary>Click to see solution</summary>

```python
# From Challenge 1
stock_symbol = "AAPL"
buying_price = 150.00
current_market_price = 165.50
shares_owned = 10

# Calculations
total_investment = buying_price * shares_owned
current_value = current_market_price * shares_owned
profit = current_value - total_investment
profit_percentage = (profit / total_investment) * 100
is_profitable = profit > 0

# Print results
print(f"\n=== {stock_symbol} P&L Report ===")
print(f"Total Investment: ${total_investment:.2f}")
print(f"Current Value: ${current_value:.2f}")
print(f"Profit/Loss: ${profit:.2f}")
print(f"Profit %: {profit_percentage:.2f}%")
print(f"Is Profitable: {is_profitable}")
```
</details>

---

### Challenge 3: Future Scenario Analysis
**Task:** Calculate what your profit would be if the stock price increases by $10.

**Requirements:**
- Use the variables from Challenge 2
- Calculate future price (+$10)
- Calculate future value
- Calculate future profit
- Calculate future profit percentage

<details>
<summary>Click to see solution</summary>

```python
# Continuing from Challenge 2...
future_price = current_market_price + 10
future_value = future_price * shares_owned
future_profit = future_value - total_investment
future_profit_percentage = (future_profit / total_investment) * 100

# Print future scenario
print(f"\n=== Future Scenario (+$10) ===")
print(f"Future Price: ${future_price:.2f}")
print(f"Future Profit: ${future_profit:.2f}")
print(f"Future Profit %: {future_profit_percentage:.2f}%")
```
</details>

---

## Advanced Challenge (Optional)

### Challenge 4: Multi-Scenario Analysis
**Task:** Create a comparison between different price scenarios.

Calculate and display profit for:
1. Current market price
2. Price increase by $5
3. Price increase by $10
4. Price decrease by $5

<details>
<summary>Click to see solution</summary>

```python
# Base data
stock_symbol = "TSLA"
buying_price = 425.00
current_market_price = 435.80
shares_owned = 100
total_investment = buying_price * shares_owned

# Function to calculate profit at any price
def calculate_profit(price):
    value = price * shares_owned
    profit = value - total_investment
    return profit

# Calculate scenarios
current_profit = calculate_profit(current_market_price)
up_5_profit = calculate_profit(current_market_price + 5)
up_10_profit = calculate_profit(current_market_price + 10)
down_5_profit = calculate_profit(current_market_price - 5)

# Display results
print(f"=== {stock_symbol} Scenario Analysis ===")
print(f"Current price (${current_market_price:.2f}): ${current_profit:.2f}")
print(f"If +$5 (${current_market_price+5:.2f}): ${up_5_profit:.2f}")
print(f"If +$10 (${current_market_price+10:.2f}): ${up_10_profit:.2f}")
print(f"If -$5 (${current_market_price-5:.2f}): ${down_5_profit:.2f}")
```
</details>

---

## Debugging Challenge

### Challenge 5: Find the Errors
**Task:** This code has several mistakes. Can you find and fix them?

```python
# Buggy code - DO NOT RUN AS IS
my stock = "NVDA"
purchase price = 120.50
current-price = 135.00
shares = "100"

total_cost = purchase price * shares
profit = current-price - purchase price * shares
is_winning = profit = 0

print(f"Profit: {profit.2f}")
```

<details>
<summary>Click to see errors and fixes</summary>

**Errors:**

1. ❌ `my stock` - variable names can't have spaces
   - Fix: `my_stock` or `stock_symbol`

2. ❌ `purchase price` - spaces in variable name
   - Fix: `purchase_price`

3. ❌ `current-price` - hyphens not allowed
   - Fix: `current_price`

4. ❌ `shares = "100"` - should be integer, not string
   - Fix: `shares = 100`

5. ❌ Wrong profit calculation - order of operations issue
   - Fix: `profit = (current_price - purchase_price) * shares`

6. ❌ `is_winning = profit = 0` - using `=` instead of comparison
   - Fix: `is_winning = profit > 0`

7. ❌ `{profit.2f}` - missing colon
   - Fix: `{profit:.2f}`

**Corrected code:**
```python
stock_symbol = "NVDA"
purchase_price = 120.50
current_price = 135.00
shares = 100

total_cost = purchase_price * shares
profit = (current_price - purchase_price) * shares
is_winning = profit > 0

print(f"Profit: ${profit:.2f}")
```
</details>

---

## Data Type Questions

### Challenge 6: Identify Data Types
**Q:** What is the data type of each value?

```python
a = "TSLA"
b = 100
c = 435.80
d = True
e = 100.0
```

<details>
<summary>Click to see answers</summary>

**A:**
- `a = "TSLA"` → **str** (string)
- `b = 100` → **int** (integer)
- `c = 435.80` → **float** (floating point number)
- `d = True` → **bool** (boolean)
- `e = 100.0` → **float** (even though it looks like integer, the `.0` makes it a float)

You can verify with: `print(type(variable))`
</details>

---

## Math Operations Questions

### Challenge 7: Order of Operations
**Q:** What will be the result of each calculation?

```python
a = 10 + 5 * 2
b = (10 + 5) * 2
c = 100 / 4 * 2
d = 100 // 4 * 2
e = 17 % 5
```

<details>
<summary>Click to see answers</summary>

**A:**
- `a = 10 + 5 * 2` → **20** (multiplication first: 5*2=10, then 10+10=20)
- `b = (10 + 5) * 2` → **30** (parentheses first: 10+5=15, then 15*2=30)
- `c = 100 / 4 * 2` → **50.0** (left to right: 100/4=25.0, then 25.0*2=50.0)
- `d = 100 // 4 * 2` → **50** (floor division: 100//4=25, then 25*2=50)
- `e = 17 % 5` → **2** (modulo/remainder: 17÷5=3 remainder 2)
</details>

---

## Comparison Operators

### Challenge 8: True or False?
**Q:** Determine if each expression is True or False:

```python
price = 150.50
target = 160.00

a = price > 150
b = price >= 150.50
c = price < target
d = price == 150.5
e = price != target
```

<details>
<summary>Click to see answers</summary>

**A:**
- `a = price > 150` → **True** (150.50 is greater than 150)
- `b = price >= 150.50` → **True** (150.50 is equal to 150.50)
- `c = price < target` → **True** (150.50 is less than 160.00)
- `d = price == 150.5` → **True** (150.50 equals 150.5)
- `e = price != target` → **True** (150.50 is not equal to 160.00)
</details>

---

## Logic Operators

### Challenge 9: Compound Conditions
**Q:** What will each expression evaluate to?

```python
profit = 1000
loss = -500
break_even = 0

a = profit > 0 and loss < 0
b = profit > 0 or loss > 0
c = not (profit > 0)
d = profit > break_even and profit > loss
e = loss < 0 or break_even > 0
```

<details>
<summary>Click to see answers</summary>

**A:**
- `a = profit > 0 and loss < 0` → **True** (both conditions are true)
- `b = profit > 0 or loss > 0` → **True** (first condition is true, that's enough for OR)
- `c = not (profit > 0)` → **False** (profit > 0 is True, NOT True is False)
- `d = profit > break_even and profit > loss` → **True** (both are true)
- `e = loss < 0 or break_even > 0` → **True** (first condition is true)
</details>

---

## Reflection Questions

### Post-Learning Questions

After completing Day 1, reflect on these:

1. **What's the purpose of using different data types?**
   - Each type serves a specific purpose (text, numbers, true/false)
   - Using the right type makes operations work correctly
   - Example: Can't do math on strings

2. **Why use f-strings instead of just print()?**
   - Combines text and variables in one line
   - Formats numbers (decimal places, currency, etc.)
   - More readable and maintainable

3. **When would you use each comparison operator?**
   - `==` for exact equality
   - `>` and `<` for ranges
   - `>=` and `<=` for inclusive ranges
   - `!=` for "not equal"

4. **How does the boolean shortcut make code better?**
   - Less verbose (fewer lines)
   - More Pythonic (idiomatic)
   - Easier to read once you understand it

---

## Scoring Guide

- **10-12 correct:** Excellent! You've mastered Day 1 concepts.
- **7-9 correct:** Good job! Minor review recommended.
- **4-6 correct:** Review the concepts and try the challenges again.
- **0-3 correct:** Take time to practice more with variables and operators.

---

## Next Steps

If you answered most questions correctly:
✅ You're ready for Day 2 (Loops, Lists, and Dictionaries)!

If you struggled with some:
🔄 Review the relevant sections in `basic_variable.py`
🔄 Try modifying the code with different values
🔄 Practice writing your own calculations

---

*Remember: Learning to code is about practice and repetition. If something doesn't click immediately, that's completely normal. Keep experimenting and asking questions!*

**Last Updated:** Day 1 - Variables, Data Types & Operators
