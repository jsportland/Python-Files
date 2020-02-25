# user_rot.py
# Rot Cypher based on user choice
# Jeff Smith

import string


def rot(my_str):
    eng = string.ascii_letters
    # Create empty string for output
    crypt = ""
    for char in my_str:
        crypt += eng[(eng.find(char) + my_rot) % 26]
    return crypt


# Ask user for input string to convert
my_str = input('What word would you like to obfuscate today? ')
# Ask user for number of places to shift
my_rot = int(input('How may characters would you like to shift your word? '))
# Shift string and display results to console
print('Thank you. Your obfuscated word is: ' + rot(my_str))
