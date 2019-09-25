'''
Create a program that asks the user for a number and then prints out a list of
all the divisors of that number. (If you don’t know what a divisor is, it is a
number that divides evenly into another number. For example, 13 is a divisor of
26 because 26 / 13 has no remainder.)
'''

##ask number
number = int(input('Please enter your number: '))

##create a loop od list of possible dividers
for x in range(1,int(number+1)):

    ##condition - if modulo divide = 0 - this is divider
    if int(number) % x == 0:
        print(x)


