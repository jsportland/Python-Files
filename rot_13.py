# Rot 13 Cypher
# Jeff Smith

import string


def rot13(my_str):
    eng = string.ascii_letters
    crypt = ""
    for char in my_str:
        crypt += eng[(eng.find(char)+13) % 26]
    return crypt


# Ask user for input string to convert
my_str = input('What word would you like to obfuscate today? ')
# Shift string and display results to console
print('Your obfuscated word is: ' + rot13(my_str))
