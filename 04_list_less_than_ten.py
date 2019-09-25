'''
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less
than 5.

Extras:

    -Instead of printing the elements one by one, make a new list that has all
    the elements less than 5 from this list in it and print out this new list.
    -Ask the user for a number and return a list that contains only elements
    from the original list a that are smaller than that number given by the
    user.
'''

##create a list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

##ask number to return numbers smaller than that number
number = input('Enter number, if you dont give a number we give back you \
number smaller than 5: ')

##create empty list for elements less than 5
less = []

##check value of number
if number == '':
    

    ##iteration for every element in the list
    for element in a:

        ##check condition - less than 5
        if element < 5:
            ##apply new elements to less list
            less.append(element)

##if value is not empty we calculate by user number
else:
    for element in a:
        if element < int(number):
            less.append(element)

##print less list
print(less)

