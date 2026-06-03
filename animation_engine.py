import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from vector_engine import Vectors

M = 20000
t_raw = np.linspace(0, 2*np.pi, M, endpoint=False)
deltoid_points = (2*np.cos(t_raw) + np.cos(2*t_raw)) + 1j * (2*np.sin(t_raw) - np.sin(2*t_raw))

n_vectors = 50
scribe_mind = Vectors(points=deltoid_points, n=n_vectors)

total_frames = 500

fig, ax = plt.subplots(figsize=(8, 8))
fig.patch.set_facecolor('#000000')
ax.set_facecolor('#000000')
ax.set_aspect('equal')
ax.axis('off')

min_x, max_x = np.min(deltoid_points.real), np.max(deltoid_points.real)
min_y, max_y = np.min(deltoid_points.imag), np.max(deltoid_points.imag)
pad_x = (max_x - min_x) * 0.1
pad_y = (max_y - min_y) * 0.1

ax.set_xlim(min_x - pad_x, max_x + pad_x)
ax.set_ylim(min_y - pad_y, max_y + pad_y)

ax.plot(deltoid_points.real, deltoid_points.imag, color='#E6E6FA', alpha=0.10, lw=1.5)

vector_lines, = ax.plot([], [], color='#C3B1E1', lw=1.2, marker='o', markersize=3, markerfacecolor='#E6E6FA')
drawn_path, = ax.plot([], [], color='#B57EDC', lw=2)

path_x = []
path_y = []

def init():
    vector_lines.set_data([], [])
    drawn_path.set_data([], [])
    return vector_lines, drawn_path

def update(frame):
    t = frame * (2*np.pi / total_frames)
    
    v_k = scribe_mind.vector_t(t)
    
    chain = np.cumsum(np.concatenate(([0j], v_k)))
    
    vector_lines.set_data(chain.real, chain.imag)
    
    path_x.append(chain[-1].real)
    path_y.append(chain[-1].imag)
    drawn_path.set_data(path_x, path_y)
    
    return vector_lines, drawn_path

ani = animation.FuncAnimation(fig, update, frames=total_frames, init_func=init, blit=True, interval=20)

plt.show()