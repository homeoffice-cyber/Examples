from random import random

from matplotlib import pyplot as plt

plt.ion()
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim([-1, 1])

for i in range(100):
    x = i
    y = random()
    # plt.gca().cla() # optionally clear axes
    plt.plot(x, y, '.')
    plt.title(str(i))
    plt.draw()
    plt.pause(0.1)

plt.show(block=True)