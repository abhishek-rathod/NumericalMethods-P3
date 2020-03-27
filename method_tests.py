"""This module is used to test the rk4 and modified Euler's
using another problem

the problem is of an oscillating mass attached to a spring of stiffness 0.5
and damper with damping coefficient 0.2

the mass is let go from some position y = 1
"""

from methods import *
t = 0.0
tstop = 60.0
y = np.array([1.0, 0.0])
h = 0.01
T, Y = rungakutta4(test_method, t, y, tstop, h)
T1, Y1 = modified_eulers(test_method, t, y, tstop, h)


plt.plot(T1, Y1[:, 0], 'g-', label='Modified eulers')
plt.plot(T, Y[:, 0], 'b-', label='RK4')
plt.ylabel('Position')
plt.xlabel('Time')
plt.legend()
plt.grid(True)
plt.show()
