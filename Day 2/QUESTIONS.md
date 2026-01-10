# Day 2 Practice Questions

## 📝 Self-Assessment Questions

After completing Day 2, test your understanding with these questions. Try to answer them without looking back at your notes!

---

## Quick Check Questions

### 1. List Basics
**Q:** How do you access the last item in a list without knowing its length?
<details>
<summary>Click to see answer</summary>

**A:** Use negative indexing: `my_list[-1]`

Example:
```python
stocks = ["TSLA", "AAPL", "NVDA"]
last = stocks[-1]  # "NVDA"
```
</details>

### 2. For Loop Syntax
**Q:** What's wrong with this code?
```python
stocks = ["TSLA", "AAPL", "NVDA"]
for stock in stocks
    print(stock)
```
<details>
<summary>Click to see answer</summary>

**A:** Missing colon (`:`) after the for statement.

**Correct:**
```python
for stock in stocks:
    print(stock)
```
</details>

### 3. While Loop Danger
**Q:** Why is this dangerous?
```python
count = 0
while count < 10:
    print(count)
```
<details>
<summary>Click to see answer</summary>

**A:** It's an infinite loop! `count` never increases, so the condition `count < 10` is always true.

**Fix:**
```python
count = 0
while count < 10:
    print(count)
    count += 1  # Increment the counter
```
</details>

### 4. Dictionary Access
**Q:** What's the difference between `stock["price"]` and `stock.get("price")`?
<details>
<summary>Click to see answer</summary>

**A:** 
- `stock["price"]` raises a `KeyError` if the key doesn't exist
- `stock.get("price")` returns `None` if the key doesn't exist
- `stock.get("price", 0)` returns `0` (or any default) if the key doesn't exist

**Example:**
```python
stock = {"symbol": "TSLA"}

# This raises KeyError:
# price = stock["price"]

# This is safe:
price = stock.get("price", 0)  # Returns 0
```
</details>

### 5. Zip Function
**Q:** What does `zip()` do?
<details>
<summary>Click to see answer</summary>

**A:** `zip()` combines multiple lists into tuples, pairing items at the same index.

**Example:**
```python
symbols = ["TSLA", "AAPL"]
prices = [435.80, 165.50]

for symbol, price in zip(symbols, prices):
    print(f"{symbol}: ${price}")

# Output:
# TSLA: $435.80
# AAPL: $165.50
```
</details>

---

## Concept Application Questions

### 6. List Methods
**Q:** Given `stocks = ["TSLA", "AAPL", "NVDA"]`, write code to:
- Add "MSFT" to the end
- Remove "AAPL"
- Check if "GOOGL" is in the list

<details>
<summary>Click to see answer</summary>

**A:**
```python
stocks = ["TSLA", "AAPL", "NVDA"]

# Add "MSFT" to the end
stocks.append("MSFT")

# Remove "AAPL"
stocks.remove("AAPL")

# Check if "GOOGL" is in the list
if "GOOGL" in stocks:
    print("Found GOOGL")
else:
    print("GOOGL not in list")
```
</details>

### 7. Loop with Index
**Q:** How would you print each stock with its position number (starting from 1)?
```python
stocks = ["TSLA", "AAPL", "NVDA"]
# Expected output:
# 1. TSLA
# 2. AAPL
# 3. NVDA
```

<details>
<summary>Click to see answer</summary>

**A:** Multiple ways:

**Method 1: Using range()**
```python
for i in range(len(stocks)):
    print(f"{i+1}. {stocks[i]}")
```

**Method 2: Using enumerate()**
```python
for i, stock in enumerate(stocks, start=1):
    print(f"{i}. {stock}")
```

**Method 3: Manual counter**
```python
counter = 1
for stock in stocks:
    print(f"{counter}. {stock}")
    counter += 1
```
</details>

### 8. Dictionary Update
**Q:** What's wrong with this code?
```python
stock = {"symbol": "TSLA", "price": 435.80}
new_data = {"shares": 100, "sector": "Tech"}

# Want to combine both dictionaries
stock = stock + new_data
```

<details>
<summary>Click to see answer</summary>

**A:** You can't use `+` operator on dictionaries!

**Correct methods:**

**Method 1: .update()**
```python
stock.update(new_data)
```

**Method 2: Merge operator (Python 3.9+)**
```python
stock = stock | new_data
```

**Method 3: Unpacking**
```python
stock = {**stock, **new_data}
```

**Method 4: Manual**
```python
stock["shares"] = 100
stock["sector"] = "Tech"
```
</details>

---

## Coding Challenges

### Challenge 1: Filter Profitable Stocks
**Task:** Given a list of stocks with their profit/loss, create a new list containing only profitable stocks.

```python
stocks = [
    {"symbol": "TSLA", "profit": 1080},
    {"symbol": "AAPL", "profit": -200},
    {"symbol": "NVDA", "profit": 500},
    {"symbol": "MSFT", "profit": -100}
]

# Create a list of only profitable stocks
```

<details>
<summary>Click to see solution</summary>

**Solution 1: Using a for loop**
```python
profitable_stocks = []

for stock in stocks:
    if stock["profit"] > 0:
        profitable_stocks.append(stock)

print(profitable_stocks)
# [{"symbol": "TSLA", "profit": 1080}, {"symbol": "NVDA", "profit": 500}]
```

**Solution 2: Using list comprehension (advanced)**
```python
profitable_stocks = [stock for stock in stocks if stock["profit"] > 0]
```
</details>

---

### Challenge 2: Find Maximum
**Task:** Find the stock with the highest price.

```python
portfolio = [
    {"symbol": "TSLA", "price": 435.80},
    {"symbol": "AAPL", "price": 165.50},
    {"symbol": "NVDA", "price": 520.30}
]
```

<details>
<summary>Click to see solution</summary>

**Solution:**
```python
max_stock = portfolio[0]  # Start with first stock
max_price = portfolio[0]["price"]

for stock in portfolio:
    if stock["price"] > max_price:
        max_price = stock["price"]
        max_stock = stock

print(f"Highest price: {max_stock['symbol']} at ${max_price:.2f}")
```

**Alternative using built-in max():**
```python
max_stock = max(portfolio, key=lambda x: x["price"])
print(f"Highest price: {max_stock['symbol']} at ${max_stock['price']:.2f}")
```
</details>

---

### Challenge 3: Count Occurrences
**Task:** Count how many times each stock appears in a transaction list.

```python
transactions = ["TSLA", "AAPL", "TSLA", "NVDA", "TSLA", "AAPL"]

# Expected output: {"TSLA": 3, "AAPL": 2, "NVDA": 1}
```

<details>
<summary>Click to see solution</summary>

**Solution:**
```python
counts = {}

for stock in transactions:
    if stock in counts:
        counts[stock] += 1
    else:
        counts[stock] = 1

print(counts)
# {"TSLA": 3, "AAPL": 2, "NVDA": 1}
```

**Alternative using .get():**
```python
counts = {}

for stock in transactions:
    counts[stock] = counts.get(stock, 0) + 1
```
</details>

---

### Challenge 4: Average Calculation
**Task:** Calculate the average price across all stocks in the portfolio.

```python
portfolio = [
    {"symbol": "TSLA", "price": 435.80},
    {"symbol": "AAPL", "price": 165.50},
    {"symbol": "NVDA", "price": 520.30}
]
```

<details>
<summary>Click to see solution</summary>

**Solution:**
```python
total_price = 0

for stock in portfolio:
    total_price += stock["price"]

average_price = total_price / len(portfolio)
print(f"Average price: ${average_price:.2f}")
```

**Alternative using sum():**
```python
prices = [stock["price"] for stock in portfolio]
average_price = sum(prices) / len(prices)
```
</details>

---

### Challenge 5: Nested Loops
**Task:** Print all possible pairs of stocks (combinations).

```python
stocks = ["TSLA", "AAPL", "NVDA"]

# Expected output:
# TSLA - AAPL
# TSLA - NVDA
# AAPL - NVDA
```

<details>
<summary>Click to see solution</summary>

**Solution:**
```python
stocks = ["TSLA", "AAPL", "NVDA"]

for i in range(len(stocks)):
    for j in range(i + 1, len(stocks)):
        print(f"{stocks[i]} - {stocks[j]}")
```

**Explanation:** 
- Outer loop: index `i` goes 0, 1, 2
- Inner loop: index `j` starts at `i + 1` to avoid duplicates
- This ensures we only get unique pairs
</details>

---

## Debugging Challenges

### Challenge 6: Fix the Bugs
**Task:** This code has several errors. Find and fix them all.

```python
# Calculate total portfolio value
portfolio = [
    {"symbol": "TSLA" "price": 435.80, "shares": 100},
    {"symbol": "AAPL", "price": 165.50, "shares": 50}
]

total_value = 0

for stock in portfolio
    value = stock["price"] * stock[shares]
    total_value += value

print(f"Total: ${total_value.2f}")
```

<details>
<summary>Click to see errors and fixes</summary>

**Errors:**

1. ❌ Line 3: Missing comma after `"TSLA"`
   ```python
   {"symbol": "TSLA", "price": 435.80, "shares": 100}
   ```

2. ❌ Line 8: Missing colon after for statement
   ```python
   for stock in portfolio:
   ```

3. ❌ Line 9: `shares` should be a string `"shares"`
   ```python
   value = stock["price"] * stock["shares"]
   ```

4. ❌ Line 12: Missing colon in f-string format
   ```python
   print(f"Total: ${total_value:.2f}")
   ```

**Corrected code:**
```python
portfolio = [
    {"symbol": "TSLA", "price": 435.80, "shares": 100},
    {"symbol": "AAPL", "price": 165.50, "shares": 50}
]

total_value = 0

for stock in portfolio:
    value = stock["price"] * stock["shares"]
    total_value += value

print(f"Total: ${total_value:.2f}")
```
</details>

---

## Advanced Challenges (Optional)

### Challenge 7: Portfolio Rebalancing
**Task:** You want each stock to be 33.33% of your portfolio. Calculate how many shares to buy/sell.

```python
portfolio = [
    {"symbol": "TSLA", "price": 435.80, "shares": 100},
    {"symbol": "AAPL", "price": 165.50, "shares": 50},
    {"symbol": "NVDA", "price": 520.30, "shares": 75}
]

# Calculate total portfolio value
# Determine target value per stock (33.33%)
# Calculate shares needed for each stock
# Print buy/sell recommendations
```

<details>
<summary>Click to see solution</summary>

**Solution:**
```python
# Calculate current total value
total_value = 0
for stock in portfolio:
    total_value += stock["price"] * stock["shares"]

# Target value per stock (equal weight)
target_value_per_stock = total_value / len(portfolio)

print(f"Total Portfolio: ${total_value:.2f}")
print(f"Target per stock: ${target_value_per_stock:.2f}\n")

# Calculate rebalancing
for stock in portfolio:
    current_value = stock["price"] * stock["shares"]
    target_shares = target_value_per_stock / stock["price"]
    shares_diff = target_shares - stock["shares"]
    
    print(f"{stock['symbol']}:")
    print(f"  Current: {stock['shares']} shares (${current_value:.2f})")
    print(f"  Target: {target_shares:.0f} shares (${target_value_per_stock:.2f})")
    
    if shares_diff > 0:
        print(f"  Action: BUY {shares_diff:.0f} shares")
    elif shares_diff < 0:
        print(f"  Action: SELL {-shares_diff:.0f} shares")
    else:
        print(f"  Action: HOLD (balanced)")
    print()
```
</details>

---

## Reflection Questions

### Post-Learning Questions

1. **When would you use a list vs. a dictionary?**
   - List: Ordered collection, access by position
   - Dictionary: Key-value pairs, access by name

2. **When would you use a for loop vs. a while loop?**
   - For loop: When you know how many iterations (iterate over collection)
   - While loop: When you don't know iterations (condition-based)

3. **How do you avoid infinite loops?**
   - Always have a condition that eventually becomes False
   - Increment counters
   - Use break statements when needed
   - Test your loop conditions

4. **What's the benefit of using dictionaries for stock data?**
   - Groups related data together
   - Access by meaningful names (not positions)
   - Easy to add new fields
   - Self-documenting code

---

## Scoring Guide

- **15-17 correct:** Excellent! You've mastered Day 2 concepts.
- **12-14 correct:** Good! Minor review recommended.
- **8-11 correct:** Review the concepts and try challenges again.
- **0-7 correct:** Take time to practice more with loops and dictionaries.

---

## Next Steps

If you can complete these challenges:
✅ You're ready for Day 3 (Functions, File I/O, Error Handling)

If you struggled:
🔄 Practice more with loops and dictionaries
🔄 Review the Day 2 exercises
🔄 Try creating your own mini-projects

---

*Remember: The best way to learn programming is through practice. Build things, break things, fix things. That's how you truly learn!*

**Last Updated:** Day 2 - Loops, Lists & Dictionaries
