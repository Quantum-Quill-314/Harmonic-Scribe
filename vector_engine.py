import numpy as np
import cmath as cm 
# tricuspoid plot generation
M = 10000   #number of discrete points
t = np.linspace(0, 2*np.pi, M, endpoint=False)
points = (2*np.cos(t) + np.cos(2*t)) + 1j * (2*np.sin(t) - np.sin(2*t))

n = 5   #number of vectors
k = np.arange(n) - (n // 2)
k = k.reshape(-1,1)
t = t.reshape(1,-1)
rotation_matrix = np.exp(-1j*k*t)
c_k = np.sum(points*rotation_matrix, axis = 1)/M

