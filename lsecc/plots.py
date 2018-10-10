__author__ = 'erez'

import math
import matplotlib.pyplot as plt
import bounds
import numpy



def my_delta(rate):
    n=100000
    d= n/2+rate*n*n*math.log(n)/(math.sqrt(math.exp(math.log(n)+math.log(math.log(n)))))
    delta = d/n
    if delta>1:
        delta=1
    return delta

fig = plt.figure(1)
axes = plt.gca()
axes.set_xlim([0.5,1.0])
axes.set_ylim([0,0.1])
plt.xlabel('rel distance')
plt.ylabel('rate')
x=numpy.arange(0.0,0.5,0.001)
plt.plot([bounds.gv_bin(dd) for dd in x], x)
plt.plot([my_delta(dd) for dd in x],x)
plt.show()
