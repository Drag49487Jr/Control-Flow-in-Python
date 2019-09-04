# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years:
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input()

x = int(input('Enter a dogs age: '))
dog_years = 0
for num in range(1, x + 1):
    if num == 0:
        continue
    elif num == 1:
        dog_years += 10
    elif num == 2:
        dog_years += 10
    else:
        dog_years += 7
print('The dogs age in dog years is ' + str(dog_years))
