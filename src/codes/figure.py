import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
# Use our custom style
plt.style.use('pusheen')

img = np.asarray(Image.open('../../img/pusheen.jpg'))
fig, ax = plt.subplots()


ax.set_title('Pusheen theme', fontdict = {'family':'fantasy'})
ax.set_xlabel('Sweetness [px]')
ax.set_ylabel('Softness [px]')
imgplot = ax.imshow(img)
plt.show()
