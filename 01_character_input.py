'''
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they
will turn 100 years old.
'''



#import datetime modul to get current date
import datetime

#ask users name
name = input('Please enter your name: ')

#ask users age
age = input('Please enter your age: ')

#check enter value by user, if this is not integer they need to enter it again
while not age.isdecimal():
    age = input('This is not integer value. Please enter your age again: ')

#get current date
now = datetime.datetime.now()

#calculate difference between age and 100 years
difference = 100 - int(age)

#show exactly year that user will turn 100 years old
print('Hello %s, you will turn 100 years old in %s year' \
      % (name, str(now.year+difference)))
