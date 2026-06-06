# Average Calculator Algorithm
# Author: Angela [Your Last Name]

# Step 1: Ask the user how many numbers they want to average
n = int(input("How many numbers do you want to average? "))

total = 0
i = 1

# Step 2: Loop to collect each number
while i <= n:
    number = float(input(f"Enter number {i}: "))
    total = total + number
    i = i + 1

# Step 3: Calculate and display the average
average = total / n
print(f"\nSum: {total}")
print(f"Average: {average:.2f}")
