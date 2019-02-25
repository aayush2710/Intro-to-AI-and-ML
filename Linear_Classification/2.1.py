#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 19:47:57 2019

@author: aayush
"""

import numpy as np, matplotlib.pyplot as plt

x = np.linspace(-4,4,30)
simlen = int(1e5)
err = []
n = np.random.normal(0,1,simlen)
for i in range(30):
    err_ind = np.nonzero(n <x[i])
    err_n = np.size(err_ind)
    err.append(err_n/simlen)
    
plt.plot(x.T,err)
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.show()
