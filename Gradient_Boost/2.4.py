#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 20:17:30 2019

@author: aayush
"""


#Gradient Descent
#By GVV Sharma, October 25, 2018
#Algo from Wikipedia
L = [1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6]
for c in L:
    cur_x = 1 # The algorithm starts at x=1
    gamma = 0.01 # step size multiplier
    precision = 0.00001
    previous_step_size = 1 
    max_iters = 10000 # maximum number of iterations
    iters = 0 #iteration counter
    
    df = lambda x: 3*x**2 - 3*c
    
    while (previous_step_size > precision) & (iters < max_iters):
        prev_x = cur_x
        cur_x -= gamma * df(prev_x)
        previous_step_size = abs(cur_x - prev_x)
        iters+=1

    print("The local minimum occurs at", cur_x)