import numpy as np
A = np.array([-2,2])
B = np.array([1,3])
C=np.array([4,-1])
b = (np.linalg.norm(C-A))
c=(np.linalg.norm(A-B))
a = (np.linalg.norm(B-C))
W = (a*A+b*B)/a+b
U = (c*C+b*B)/c+b
V = (a*A+c*C)/a+c

print(np.linalg.norm(A-U))
print(np.linalg.norm(B-V))
print(np.linalg.norm(C-W))




