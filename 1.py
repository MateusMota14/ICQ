import numpy as np
import matplotlib.pyplot as plt
# Testing if the roots can be real

x = np.linspace(-100,100,1000)
y = x*4 + 2*x*2 + 1

plt.plot(x,y)
plt.show()