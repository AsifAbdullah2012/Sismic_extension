import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Create a figure and an axis
fig, ax = plt.subplots()

# Initialize a line or plot
line, = ax.plot([], [], lw=3)

# Limits of the axis
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)

# Data storage
x_data, y_data = [], []

# Update function
def update(frame):
    x_data.append(frame)
    y_data.append(np.sin(frame))
    line.set_data(x_data, y_data)
    return line,

# Animation
ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 100), blit=True)

plt.show()
