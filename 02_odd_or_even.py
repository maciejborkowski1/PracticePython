'''
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user.
Extras:
-If the number is a multiple of 4, print out a different message.
-Ask the user for two numbers: one number to check (call it num)
and one number to divide by (check). If check divides evenly into num
tell that to the user. If not, print a different appropriate message.
'''

#ask number
number = input('Please type a number, and we check it this is odd or even: ')
#check the number is integer
while not number.isdecimal():
    number = (input('This is not integer number. Please enter a valid value: '))

#ask number to divide by
devide = input('Please type a number to divide by: ')

#check if user enter any check value, if check is empty we do it in old way
if devide == '':

    #check the number modulo divide by 2, if the remainder is 0, number is even
    #and divided by 4
    if int(number) % 4 == 0:
        print('%d is divided by 4, and its even' % int(number))

    #check the number modulo divide by 2, if the remainder is 0, number is even
    elif int(number) % 2 == 0:
        print('%d is even' % int(number))

    #else number is odd
    else:
        print('%d is odd' % int(number))

#else devide is not empty so we do it second extra task
else:
    #for start we should check the devide is integer
    while not devide.isdecimal():
        devide = (input('This is not integer number. Please enter a valid value: '))

    #now we modulo divide - number x devide
    if int(number) % int(devide) == 0:
        print('%d divides evenly into %d' % (int(number), int(devide)))
    else:
        print('%d NOT divides evenly into %d, we have some reminder in this calculate' % (int(number), int(devide)))



