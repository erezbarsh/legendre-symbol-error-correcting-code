__author__ = 'erez'

from fractions import gcd
#simple primes generator using eratosthene sieve
class Primes:
    primes_list = []

    def __init__(self,n):
        self.gen(n)



    def gen(self,n):
        while len(self.primes_list) < n:
            self.add_prime()


    def add_prime(self):
        if len(self.primes_list) == 0:
            self.primes_list.append(2)
            return
        prevp = self.primes_list[len(self.primes_list)-1]
        nextp = prevp+1
        while(not self.is_prime(nextp)):
            nextp = nextp+1
        self.primes_list.append(nextp)

    # assuming that all primes smaller than p are in primes
    def is_prime(self,q):
        for p in self.primes_list:
            if gcd(p,q)>1:
                return False
        return True



    def primes_3mod4(self):
        primes_list_3_mod4=[]
        for p in self.primes_list:
            if (p%4 == 3):
                primes_list_3_mod4.append(p)
        return primes_list_3_mod4


    def primes_1mod4(self):
        primes_list_1_mod4=[]
        for p in self.primes_list:
            if (p%4 == 1):
                primes_list_1_mod4.append(p)
        return primes_list_1_mod4


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


