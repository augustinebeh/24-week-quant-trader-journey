# 1. Start with a price of $100
# 2. Use a while loop to simulate price increases of $5 per day
# 3. Stop the loop when the price reaches or exceeds $150
# 4. Print the price at each day
# 5. Print how many days it took to reach the target price

price = 100
daily_increment = 5
target_price = 150
i = 0

print("-- Printing the price each day --")
while (target_price > price):
   print(f"Day {i}: ${price}")
   price += daily_increment
   i += 1

print(f"Day {i}: ${price}")
print(f"It took {i} days to reach or exceed the ${target_price} target.")
 