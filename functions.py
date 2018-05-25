import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-8, 5, 800)
y = [np.exp(i) for i in x]
plt.plot(x, y)
plt.show()