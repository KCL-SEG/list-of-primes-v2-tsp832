"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    count = 2
    if number_of_primes <= 0:
        raise ValueError
    while (len(list)) != number_of_primes:
        if isPrime(count):
            list.append(count)
        count +=1
    return list


def isPrime(n):
    if (n == 2 or n == 3 or n == 5):
        return True

    if (n % 2 == 0 or n % 3 == 0 or n % 5 == 0):
        return False
    
    i = 5
    while (i*i<n):
        if ((n % i == 0) or (n % (i + 2) == 0)):
            return False
        i+=6

    return True
