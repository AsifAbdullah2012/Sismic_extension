import matplotlib.pyplot as plt
import random
import time

plt.ion()  # Enable interactive mode
fig, ax = plt.subplots()
y_data = []

while True:
    y_data.append(random.randint(0, 10))  # Simulate data change
    ax.clear()  # Clear previous data
    ax.plot(y_data)  # Plot new data
    plt.draw()  # Redraw the graph
    plt.pause(0.1)  # Pause briefly to show updates
    time.sleep(1)  # Simulate time delay for data update
