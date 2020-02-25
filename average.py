# average.py
# Find the average in a given list of numbers
# Jeff Smith

import math

nums = [5, 0, 8, 3, 4, 1, 6]

for i in range(len(nums)):
    avg = (sum(nums)/len(nums))
avg = round(avg, 1)
print(avg)
