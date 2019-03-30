import numpy as np
import matplotlib.pyplot as plt

def midpoint(B,C):
    D=(B+C)/2
    return D

A = np.matrix('-2;2')
B = np.matrix('1;3')
C = np.matrix('4;-1')

print(midpoint(B,C))
print(midpoint(A,B))
print(midpoint(C,A))
