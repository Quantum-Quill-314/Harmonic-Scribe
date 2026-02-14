import numpy as np
import json

#Generating the Tricuspoid points for test

N = 1000
theta = np.linspace(0,  2*np.pi, N, endpoint = False)

x = 2*np.cos(theta) + np.cos(2*theta)
y = 2*np.sin(theta) - np.sin(2*theta)

#complex points:
points = x +1j*y
print(type(points))

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

amplitudes = np.abs(X_k)
phases = np.angle(X_k)
frequencies = np.arange(-50, 51)

circles = []
for i in range(len(X_k)):
    circles.append({
        "freq": int(frequencies[i]), # The 'k' value
        "radius": float(np.abs(X_k[i])), # Magnitude
        "phase": float(np.angle(X_k[i])) # Angle in radians
    })

circles.sort(key=lambda x: x["radius"], reverse=True)

# Package the data for Harmonic Scribe
output_data = {
    "name": "Tricuspoid Test",
    "total_points": N,
    "circles": circles
}

# Save it to a file in your project folder
with open("tricuspoid_dna.json", "w") as f:
    json.dump(output_data, f, indent=4)