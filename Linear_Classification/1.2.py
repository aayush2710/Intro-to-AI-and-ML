#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 19:27:13 2019

@author: aayush
"""

import numpy as np
from gaussian_no import *

simlen = int(1e5)
n = np.zeros(simlen)
for i in range(simlen):
    n[i]+=Gaussian()
    
mean = np.sum(n)/simlen
print(mean)
var = np.sum(np.square(n-mean*np.ones((1,simlen))))/simlen
print(var)