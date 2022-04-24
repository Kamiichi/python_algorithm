import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % 1 == 0:
            return False
    return True

n = input('put a number: ')
is_prime(n)