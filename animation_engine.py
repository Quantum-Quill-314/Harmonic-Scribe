import numpy as np
from vector_engine import Vectors

# (The Tricuspoid/Deltoid)
M = 10000 
t_raw = np.linspace(0, 2*np.pi, M, endpoint=False)
deltoid_points = (2*np.cos(t_raw) + np.cos(2*t_raw)) + 1j * (2*np.sin(t_raw) - np.sin(2*t_raw))
n_vectors = 5
scribe_mind = Vectors(points=deltoid_points, n=n_vectors)
