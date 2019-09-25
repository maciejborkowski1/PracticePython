'''
Write a program (function!) that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates.

Extras:

    Write two different functions to do this - one using a loop and
    constructing a list, and another using sets.
    Go back and do Exercise 5 using sets, and write the solution for that in a
    different function.
'''

def listRemoveDuplicates(x = [1, 1, 3, 3, 5, 5, 5, 11, 11, 11, 11]):
    newList = []
    for i in x:
        if i not in newList:
            newList.append(i)
    return newList

## nie działa jak powinno, zwrot wartości funkcji do ogarniecia
def listRemoveDupSET(x = [1, 1, 3, 3, 5, 5, 5, 11, 11, 11, 11]):
    return list(set(x))



