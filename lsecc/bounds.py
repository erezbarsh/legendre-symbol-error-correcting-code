__author__ = 'erez'

import math



def n_over_k(n,k):
    if(k==0 or n==k):
        return 1
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))


# GV bound
def gv_A_q_n_d(n,q,d):
    s=0
    for idx in range(d):
        s=s+n_over_k(n,idx)*math.pow(q-1,idx)
    if(s==0):
        s=1
    return math.pow(q,n)/s


def gv_bin(delta):
    return gv(2,delta)

def gv(q,delta):
    n = 1000
    d= (int)(math.ceil(n*delta))
    return math.log(gv_A_q_n_d(n,q,d),q)/n

# Hamming bound
def hb_A_q_n_d(n,q,d):
    s=0
    t=int((d-1)/2)
    for idx in range(t+1):
        s=s+n_over_k(n,idx)*math.pow(q-1,idx)
    if(s==0):
        s=1
    return math.pow(q,n)/s

def hamming_bound(q,delta):
    n = 1000
    d= (int)(math.ceil(n*delta))
    return math.log(hb_A_q_n_d(n,q,d),q)/n

def hamming_bound_bin(delta):
    return hamming_bound(2,delta)







