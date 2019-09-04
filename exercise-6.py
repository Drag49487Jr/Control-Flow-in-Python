# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
# 2. Then propts the user to enter the day of the month:
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season>

# Hints:
# Consider using the in operator to check if a string is in a particular
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif
# ...else statement to "adjust" if
# the day number falls within a certain range.
winter = ['Dec', 'Jan', 'Feb', 'Mar']
spring = ['Mar', 'Apr', 'May', 'Jun']
summer = ['Jun', 'Jul', 'Aug', 'Sep']
fall = ['Sep', 'Oct', 'Nov', 'Dec']


month = input('Enter the month of the season (Jan-Dec): ')
day = int(input('Enter the day of the month: '))
if month in winter:
    if month == 'Dec':
        if day >= 21:
            print(f'{month} {day} is winter')
        if day < 21:
            print(f'{month} {day} is fall')

if month in spring:
    if month == 'Mar':
        if day >= 20:
            print(f'{month} {day} is spring')
        if day < 20:
            print(f'{month} {day} is winter')

if month in summer:
    if month == 'Jun':
        if day >= 20:
            print(f'{month} {day} is summer')
        if day < 20:
            print(f'{month} {day} is spring')
if month in fall:
    if month == 'Sep':
        if day >= 22:
            print(f'{month} {day} is fall')
        if day < 22:
            print(f'{month} {day} is summer')
