__author__ = 'erez'

from math import gcd
from sympy import primerange,prime

class Primes:
    odd_primes_list = None

    def __init__(self,n):
        self.gen_odd_primes(n)



    def gen_odd_primes(self, n):
        self.odd_primes_list = primerange(3, prime(n+1) + 1)


def factorization(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac


