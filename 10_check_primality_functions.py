'''
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you. Take this
opportunity to practice using functions, described below.
'''

prime = True
def primeNumber(number=17):
    for i in range (2, number):
        if number % i == 0:
            prime = False
    return prime

primeNumber()

'''
do tego trzeba wrocic, pomysl dobry, ale zwraca blad
'''
