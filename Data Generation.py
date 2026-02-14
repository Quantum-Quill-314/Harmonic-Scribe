import numpy as np

#Generating the Tricuspoid points for test

N = 1000
theta = np.linspace(0,  2*np.pi, N, endpoint = False)

x = 2*np.cos(theta) + np.cos(2*theta)
y = 2*np.sin(theta) - np.sin(2*theta)

#complex points:
points = x +1j*y

#Centring the points at origin to make the 0th vector zero
centre_of_mass = np.mean(points)
points = points - centre_of_mass

#doing the DFT
K = np.arange(-50,51).reshape(-1,1)
n_idx = np.arange(N)
exponent_matrix = np.exp(-2j*K*n_idx*np.pi/N) #vector exp tp the K*n_idx matrix
#DFT
X_k = np.dot(exponent_matrix, points)/N
print(f"Arrary completed. Size = {len(X_k)}. First 5 entries: \n{X_k[0:5]}")