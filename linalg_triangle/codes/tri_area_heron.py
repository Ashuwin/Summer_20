import numpy as np 
import matplotlib.pyplot as plt
from coeffs import *
import subprocess
import shlex

P = np.array([-5,-1])
Q = np.array([3,-5])
R = np.array([5,2])

p = np.linalg.norm(Q-R)
q = np.linalg.norm(R-P)
r = np.linalg.norm(P-Q)

s = (p+q+r)/2
area = np.sqrt(s*(s-p)*(s-q)*(s-r))

print("Area of triangle PQR: ",area)