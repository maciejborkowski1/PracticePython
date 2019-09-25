'''
Write a program that takes a list of numbers (for example,
a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last
elements of the given list. For practice, write this code inside a function.
'''


def firstLast(list=[5, 10, 15, 20, 25]):
    firstLast = [list[0], list[-1]]
    return print(firstLast)
firstLast([1,2,3,4,5])
