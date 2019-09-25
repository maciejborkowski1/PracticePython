'''
Ask the user for a string and print out whether this string is a palindrome
or not. (A palindrome is a string that reads the same forwards and backwards.)
'''

word = input('Is this palindrome? Enter your word: ')

reverse = word[::-1]

if word == reverse:
    print('%s is palindrome.' % word)
else:
    print('%s is NOT palindrome.' % word)



