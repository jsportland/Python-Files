# list_avg.py
# Average user-submitted numbers
# Jeff Smith

import math

# Create empty list
nums = []

# Ask user for numbers to evaluate
# Ensure all text is converted to lowercase
ele = input('Enter a number or type done: ').lower()
if ele == 'done':
    # If user types 'done', exit
    print('Ok. Perhaps another time.')

    # If user submits numbers, ask for further numbers
while ele != 'done':
    nums.append(ele)
    ele = input('Enter a number or type done: ').lower()

# Convert list from strings to ints
nums = [int(x) for x in nums]

# Average user input and pass results to console
print(sum(nums)/len(nums))
