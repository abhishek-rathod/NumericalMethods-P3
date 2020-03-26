import numpy as np
import matplotlib.pyplot as plt
import math
from methods import *
'''
Using rk4 to solve for velocity as a function of time
'''




'''
Now using rk4 to solve for position
y is position here and x is time
'''
x = 0.0
xstop = 10.0
y = np.array([0.0, 0.0])
h = 0.1

X, Y = rungakutta4(F, x, y, xstop, h)
plt.plot(X, Y[:, 0], label='numerical')
plt.show()
