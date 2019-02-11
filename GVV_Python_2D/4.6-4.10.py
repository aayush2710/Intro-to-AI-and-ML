import numpy as np
import math
import matplotlib.pyplot as plt
A = np.array([-2,2])
B = np.array([1,3])
C=np.array([4,-1])




def norm_vec(AB):
    return np.matmul(omat,np.matmul(AB,dvec))

def line_intersect(AD,CF):
    n1 = norm_vec(AD)
    n2=norm_vec(CF)
    N=np.vstack((n1,n2))
    p=np.zeros(2)
    p[0] = np.matmul(n1,AD[:,0])
    p[1] = np.matmul(n2,AD[:,0])
    return np.matmul(np.linalg.inv(N),p)

A = np.array([-2,-2])
B = np.array([1,3])
C=np.array([4,-1])
b = (np.linalg.norm(C-A))
c=(np.linalg.norm(A-B))
a = (np.linalg.norm(C-B))
W = (a*A+b*B)/(a+b)
U = (c*C+b*B)/(c+b)
V = (a*A+c*C)/(a+c)

AU = np.vstack((A,U)).T
CW = np.vstack((C,W)).T
BV = np.vstack((B,V)).T
dvec = np.array([-1,1])
omat= np.array([[0,1],[-1,0]])

lam_1 = np.linspace(0,1,10)
x_AB = np.zeros((2,10))
x_BC = np.zeros((2,10))
x_CA = np.zeros((2,10))
x_AU = np.zeros((2,10))
x_BV = np.zeros((2,10))
x_CW = np.zeros((2,10))


for i in range(10):
    temp1 = A+lam_1[i]*(B-A)
    x_AB[:,i] = temp1.T
    temp2 = B+lam_1[i]*(C-B)
    x_BC[:,i] = temp2.T
    temp3 = C+lam_1[i]*(A-C)
    x_CA[:,i] = temp3.T
    temp4 = U+lam_1[i]*(A-U)
    x_AU[:,i] = temp4.T
    temp5 = V+lam_1[i]*(B-V)
    x_BV[:,i] = temp5.T
    temp6 = W+lam_1[i]*(C-W)
    x_CW[:,i] = temp6.T

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')

plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_AU[0,:],x_AU[1,:],label='$AU$')
plt.plot(x_BV[0,:],x_BV[1,:],label='$BV$')
plt.plot(x_CW[0,:],x_CW[1,:],label='$CW$')



print(line_intersect(CW,BV))
print(line_intersect(AU,BV))
print(line_intersect(CW,AU))
I = np.array([1.15,0.41])
r = np.linalg.norm(U-I)
theta = np.linspace(0,2*np.pi,100)
x,y=[],[]
for i in theta:
    x.append(I[0]+r*math.cos(i))
    y.append(I[1]+r*math.sin(i))
plt.plot(x,y,label = "Ci")


