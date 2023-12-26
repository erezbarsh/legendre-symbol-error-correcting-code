__author__ = 'erez'

import math
from primes import Primes
import matplotlib.pyplot as plt
import bounds
import numpy as np
import sys
from sympy.ntheory import legendre_symbol as sympy_ls
from sympy.ntheory import jacobi_symbol as sympy_js
from sympy import primerange





def legendre_symbol(a, p):
    return sympy_ls(a,p)



def jacobi_symbol(a, m):
    return sympy_js(a,m)



def bin_arr(num, fixlen=0):
    binary = []
    while num != 0:
        bit = num % 2
        binary.append(bit)
        num = num / 2
    while(fixlen > len(binary)):
        binary.append(0)
    return binary




def gen_words(primes_arr):
    ret_words=[]
    for bin in range(pow(2,len(primes_arr))):
        ba = bin_arr(bin,len(primes_arr))
        ret_words.append(mul_pow(primes_arr,ba))
    return ret_words



def mul_pow(multipliers,powers):
    if(len(multipliers)!= len(powers)):
        return 0
    retval = 1
    for idx, val in enumerate(multipliers):
        retval = retval* pow(val,powers[idx])
    return retval

# a matrix containing the code words
def generate_code(n,k):
    primes = Primes(n+k)
    primes_list = primes.odd_primes_list
    #primes_list=primes.primes_3mod4()
    print (primes_list)

    words = gen_words(primes_list[0:k])
    primes = primes_list[k:n+k]
    print(primes_list)
    print(primes)
    code = [[legendre_symbol(w,p) for p in primes] for w in words]
    return code

# assuming a well defined code matrix
def calculate_code_distance(code):
    d=0
    if(len(code)>0):
        d=len(code[0])
    for i in range(len(code)):
        for w in code:
            if(w != code[i]):
                d=min(d,distance(w,code[i]))
    return d

def alter_to_linear(code):
    for w in code:
        for i in range(len(w)):
            if(w[i]==1):
                w[i]=0
            if(w[i]==-1):
                w[i]=1


def calculate_code_distance_linear(code):
    if(len(code)==0):
        return 0
    d=len(code[0])
    for word in code:
        wt = weight(word)
        if(wt>0 and wt<d):
            d=wt
    return d

def distance(w1,w2):
    d = 0
    if(len(w1) != len(w2)):
        return d
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            d = d+1
    return d

def weight(word):
    wt = 0
    for c in word:
        if c!=0:
            wt+=1
    return wt


def calculate_code_params(the_code):
    alter_to_linear(the_code)
    #print code[0:10]
    n = len(the_code[0])
    k = math.log(len(the_code),2)
    #d=calculate_code_distance(code)
    if(check_unique_encoding(the_code)):
        d = calculate_code_distance_linear(the_code)
    else:
        d=0
    print ("d=",d)
    print ("code (n,k,d)=",n,k,d)
    print ("code (k/n,d/n)=",k*1.0/n,d*1.0/n)
    return k*1.0/n,d*1.0/n


def calculate_ls_code_params(ln,dim):
    code = generate_code(ln,dim)
    #print code
    return calculate_code_params(code)


def plot_leg_sym_code():
    fig = plt.figure(1)
    plt.xlabel('rel distance')
    plt.ylabel('rate')
    x=np.arange(0.0,0.5,0.025)
    plt.plot(x, [bounds.gv_bin(dd) for dd in x])
    for k in range(8,9,1):
        rate,delta = calculate_ls_code_params(256,k)
        plt.plot(delta,rate,"ro")
    plt.show()

def check_unique_encoding(the_code):
    for w1 in the_code:
        cnt_similar = 0
        for w2 in the_code:
            if(w1 == w2):
                cnt_similar = cnt_similar+1
        if cnt_similar!=1:
            return False
    return True


def plot_delta_rate_fix_k():
    k=10
    rates= np.arange(0.01,1.0,0.01)
    deltas = np.array([])
    for r in rates:
        n=int(k/r)
        delta = 1.0*calculate_ls_code_params(n,k)[1]
        deltas = np.append(deltas,delta)
    print (rates)
    print (deltas)
    plt.plot(rates, deltas, 'ro', label='This paper, k=10')

    # GV bound
    gv_deltas = np.arange(0.0,0.5,0.01)
    gv_rate = np.asanyarray([bounds.gv_bin(dd) for dd in gv_deltas])
    plt.plot(gv_rate, gv_deltas, 'b-', label='GV Bound')

    # Hamming bound
    hb_rate = np.asanyarray([bounds.hamming_bound_bin(dd) for dd in gv_deltas])
    plt.plot(hb_rate, gv_deltas, 'g--', label='Hamming Bound')

    plt.xlabel('rate (k/n)')
    plt.ylabel('relative distance (d/n)')
    plt.axis([0, 1, 0, 0.5])
    plt.legend()
    plt.show()

def plot():
    plot_delta_rate_fix_k()

def test():
    print ("test")
    # plot_leg_sym_code()
    # print(jacobi_symbol(5,6))
    print(legendre_symbol(3,17))
    print(jacobi_symbol(5, 21))
    print(list(Primes(5).odd_primes_list))
    # print calculate_jacobi_code_params(16,4)
    # print check_unique_encoding(generate_jacobi_code(16,4))
    # k=10
    # print calculate_ls_code_params(64,8)

def main():
    print ("legendre symbol error corrcting code")
    try:
        n = int(sys.argv[1])
        k = int(sys.argv[2])
        print (calculate_ls_code_params(n, k))
    except:
        print ("Error runnig lsecc. \nrun: python lscode.py <code-length> <code-dimension>")




if __name__ == "__main__":
    #plot()
    test()
    # main()











