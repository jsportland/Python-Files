# lotto.py
# Pick 6-style lottery simulator
# Jeff Smith

'''
Steps
    /Loop 100,000 times, for each loop:
    /Generate a list of 6 random numbers representing the ticket
    /Subtract 2 from the balance (for price of ticket)
    /Find how many numbers match
    /Add winnings from matches to balance
    /After loop, print final balance
    /Calculate ROI
'''
import random


def wins():

    cost = 2  # Cost of lotto ticket
    count = 0  # Tally of number of tickets purchased
    # Generate random 6-digit lotto number
    lotto = random.sample(range(1, 100), 6)
    print(f'The winning numbers are: {lotto}')  # Pass lotto number to console

    while count < 1000:  # Set limit on number of attempts to 1,000
        count += 1  # Keep tally of attempts
        bal = -2  # Deduct lotto cost from balance
        # Generate random 6-digit lotto pick
        tix = random.sample(range(1, 100), 6)
        # Define the number of matches between ticket and lotto
        nums = [i for i, j in zip(tix, lotto) if i == j]

        # Define return on investment
        roi = 2 * 1000
        roi1 = bal - roi
        roi2 = roi / roi1
        roi3 = int(roi2 * 100)

        # Calculate winnings based on number of matches
        if len(nums) == 6:
            bal += 25000000
        elif len(nums) == 5:
            bal += 1000000
        elif len(nums) == 4:
            bal += 50000
        elif len(nums) == 3:
            bal += 100
        elif len(nums) == 2:
            bal += 7
        elif len(nums) == 1:
            bal = + 4

    # Pass the results to the console
    return(
        f'Based on your balance of ${bal} and the ${cost} you spent, the return on your investment is ${roi3}%')


print(wins())
