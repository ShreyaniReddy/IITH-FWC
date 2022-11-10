from sympy import*

import cvxpy as cp
import sympy as sy
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math
import mpmath as mp


#if using termux
import subprocess
import shlex
#end if

print("Verification Using Differentiation")
x = symbols ('x')
y = symbols ('y')
P = np.array([x,y])

x1 = symbols ('x1')
y1 = symbols ('y1')
A = np.array([x1,y1])

x2 = symbols ('x2')
y2 = symbols ('y2')
B = np.array([x2,y2])

x3 = symbols ('x3')
y3 = symbols ('y3')
C = np.array([x3,y3])


PA2 = (P-A)@(P-A)
PB2 = (P-B)@(P-B)
PC2 = (P-C)@(P-C)


df1 = diff(PA2,x)
df2 = diff(PB2,x)
df3 = diff(PC2,x)
dfx = df1+df2+df3
print("min of PA^2+PB^2+PC^2:")
print(dfx)

sol1 = sy.solve(dfx,x)

df4 = diff(PA2,y)
df5 = diff(PB2,y)
df6 = diff(PC2,y)
dfy = df4+df5+df6
print(dfy)
sol2 = sy.solve(dfy,y)


print(sol1)
print(sol2)

P = np.array([sol1,sol2])
P = P.reshape(2,)
print(P)

#Verification Using  cvxpy

#Declaring Variables
P = cp.Variable(pos=True, name="P")



A = np.array([0,0])
B = np.array([4,0])
C = np.array([3,4])
P = (A+B+C)/3

X = (cp.norm(P-A))**2+(cp.norm(P-B))**2+(cp.norm(P-C))**2

#constraints = [
 #    P == (A+B+C)/3]

#Problem Formulation
problem = cp.Problem(cp.Minimize(X))

#solution
problem.solve()
print(P)
print(problem.value)

