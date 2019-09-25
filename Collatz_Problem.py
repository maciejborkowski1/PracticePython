def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print (3 * number + 1)
        return 3 * number + 1
print ('-------------------------')

try:
    number = int(input('Podaj liczbę całkowitą: '))
except ValueError:
    print('Podana wartość nie jest liczbą całkowitą!')

try:
    while number != 1:
        number = collatz(number)
except NameError:
    print('Spróbuj innym razem')
