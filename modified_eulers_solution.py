"""
This moduel contains the solution using modified euler method
it imports the functions from the methods.py module
"""

from methods import *

'''using the modified eulers to solve the projectile problem
for velocity as a function of time'''

t = 0.0
tstop = 10.0
v = 0.0
h = 0.1

T, V = modified_eulers(f, t, v, tstop, h)

'''using the modified eulers to solve the projectile problem
for position as a function of time'''

x = 0.0
xstop = 10.0
y = np.array([0.0, 0.0])

X, Y = modified_eulers(F, x, y, xstop, h)


