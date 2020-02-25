# cc_val.py
# Jeff Smith
# CC validation

'''
Returns whether a string containing a credit card number is valid as a boolean
The steps are as follows:
1. Convert the input string into a list of ints
2. Slice off the check digit.
3. Reverse the digits.
4. Double every other element in the reversed list.
5. Subtract nine from numbers over nine.
6. Sum all values.
7. Take the second digit of that sum.
8. If that matches the check digit, the card number is valid.
'''

import math

# Sample CC number
cc = input('Please enter a credit card number to analyze: ')

# Convert the input string into a list of ints
ccint = [int(x) for x in '4556737586899855']
cc_num = int(cc)

# Slice off check digit.
ckdg = (ccint[slice(-1)])
slob = ccint[-1]

# Reverse the digits.
revckdg = ckdg[::-1]

# Double every other element in the reversed list.
double = revckdg[:]
double = [double[index]*2 if index % 2 == 0 else double[index]
          for index in range(len(double))]

# Subtract nine from numbers over nine.
nine = double[:]
nine = [nine[index]-9 if index >= 0 else nine[index]
        for index in range(len(nine))]

# 6. Sum all values.
sumval = sum(nine)

# 7. Take the second digit of that sum.
str_sumval = str(sumval)
new_sumval = str_sumval[-1]
int_sumval = int(str_sumval)

# 8. Check that result matches the check digit
# Match means the card number is valid.
if int_sumval / cc_num == 1:
    print(f'{cc} appears to be a valid credit card number')
else:
    print(f'{cc} is not a valid credit card number')
