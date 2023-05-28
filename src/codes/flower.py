import numpy as np
import matplotlib.pyplot as plt

plt.style.use('pusheen')

theta = np.linspace(0, 2*np.pi, 1000)
r = 3* np.sin(8 * theta)


fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta+(r<0)*np.pi, np.abs(r))
ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)

ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()
