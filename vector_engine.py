import numpy as np

class Vectors:
    def __init__(self, points, n):
        """
        The Constructor. This handles the discrete extraction phase.
        It locks the blueprint into the object's static memory.
        """
        self.points = np.array(points)
        self.M = len(self.points)
        self.n = n
        
        self.k = np.arange(self.n) - (self.n // 2)
        k_col = self.k.reshape(-1, 1)
        t_discrete = np.linspace(0, 2*np.pi, self.M, endpoint=False).reshape(1, -1)
        rotation_matrix = np.exp(-1j * k_col * t_discrete)
        # Calculating the coeffs
        self.c_k = np.sum(self.points * rotation_matrix, axis=1) / self.M

    def vector_t(self, t):
        #Takes a specific time 't' and spins all static arms forward.
        
        # Multiply the static arms (c_k) by the forward-spinning motor at time 't'
        v_k = self.c_k * np.exp(1j * self.k * t)
        
        # Returns an array of the individual rotating vectors for this exact frame
        return v_k