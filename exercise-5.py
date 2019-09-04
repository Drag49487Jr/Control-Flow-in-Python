# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it
total = 0
num1 = 0
num2 = 1

while total < 50:
    if total < 2:
        print(f'term = {total} | number = {total}')
    else:
        next_num = num1 + num2
        print(f'term = {total} | number = {next_num}')
        num1 = num2
        num2 = next_num
    total += 1
