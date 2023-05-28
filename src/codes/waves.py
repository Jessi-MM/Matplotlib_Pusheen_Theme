import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv

# Use our custom style
plt.style.use('pusheen')

fig, ax = plt.subplots()
x = np.linspace(0, 10, 100)

for i in range(0, 6):
  J = jv(i, x)
  ax.plot(x, J, label='y'+str(i))

# Set axis labels
ax.set_title('Beauty title')
ax.set_xlabel('Time [s]')
ax.set_ylabel('Position [m]')
plt.legend()
plt.show() 
