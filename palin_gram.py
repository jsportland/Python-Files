# palin_gram.py
# Jeff Smith
# Palindrome and Anagram

'''
Palindrome
check_palindrome takes a string, and returns True if the string's a palindrome, or False if it's not.
'''


def check_palindrome(wd):
    if rev == wd:
        return((wd) + ' is a palindrome')
    return((wd) + ' is not a palindrome')


wd = input('Enter a word to check if its a palindrome: ').lower
rev = wd[::-1]  # reverse the string
print(check_palindrome(wd))


'''
Anagram
Two words are anagrams of eachother if the letters of one can be rearranged to fit the other. e.g. anagram and nag a ram.
check_anagram takes two strings as parameters and returns True if they're anagrams of eachother
False if they're not.
'''


def check_anagram(wd1, wd2):

    if (sorted(wd1)) == (sorted(wd2)):
        return((wd1) + ' is an anagram of ' + (wd2))
    else:
        return((wd1) + 'and ' + (wd2) + 'are not an anagram')


wd1 = 'anagram'.replace(" ", "")
wd2 = 'nag a ram'.replace(" ", "")

print(check_anagram(wd1, wd2))
