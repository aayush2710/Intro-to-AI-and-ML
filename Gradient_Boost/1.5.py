#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 19:59:21 2019

@author: aayush
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x1 = np.linspace(2,6,10)
x2 = np.linspace(2,6,10)
y = np.zeros((10,10))
for i in range(10):
    for j in range(10):
        
        y[i,j] += (x1[i]*x2[j])
        

ax.scatter(x1, x2, y, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()