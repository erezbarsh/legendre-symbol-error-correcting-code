__author__ = 'erez'
import numpy as np
import matplotlib.pyplot as plt
from lscode import calculate_ls_code_params
import bounds





def plot_delta_rate_fix_k():
    k=10
    ns = np.arange(k*3,2**k,1)
    ns = np.insert(ns,0,10)
    ns = np.insert(ns, 0, 10)
    ns = np.insert(ns, 0, 14)
    ns = np.insert(ns, 0, 20)
    ns = np.insert(ns, 0, 27)
    # rates= np.arange(0.01,1,0.005)
    # ns = [int(k/r) for r in rates]
    # ns = np.unique(ns)
    rates = k/ns
    #
    # ns = [int(k / r) for r in rates]
    deltas = np.array([])
    for n in ns:
        delta = 1.0*calculate_ls_code_params(n,k)[1]
        deltas = np.append(deltas,delta)
    print (rates)
    print (deltas)
    plt.scatter(rates, deltas, c='red', s=5, label='This paper, k=10')

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
    plt.savefig("LSC_GV_Hamming.png", dpi=300)
    plt.show()




def plot_delta_fix_k():
    k=10
    # ns = np.arange(k,2**k,10)
    ns = np.arange(k,2**k,10)
    deltas = np.array([])
    for n in ns:
        delta = 1.0*calculate_ls_code_params(n,k)[1]*n
        deltas = np.append(deltas,delta)
    plt.bar(ns, deltas, width=10, label='code distance for k=10')
    # plt.plot(ns, ns/2, color='red', label='n/2')
    plt.xlabel('code length (n)')
    plt.ylabel('code distance (d)')
    plt.title('Legendre Symbol code - Distance vs Length for Dimension k=10')
    # plt.legend()
    plt.savefig("LSC_Distance.png", dpi=300)
    plt.show()