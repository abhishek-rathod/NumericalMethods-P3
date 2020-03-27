"""
This module contains the solution using modified euler method
it imports the functions from the methods.py module
"""

from methods import *

'''using the modified eulers to solve the projectile problem
for velocity as a function of time'''

t = 0.0
tstop = 10.0
v = 0.0
h = 0.05

T, V = modified_eulers(f, t, v, tstop, h)

'''using the modified eulers to solve the projectile problem
for position as a function of time'''

x = 0.0
xstop = 10.0
y = np.array([0.0, 0.0])

X, Y = modified_eulers(F, x, y, xstop, h)

t = np.linspace(0, 10, 100)
V_analytic = []
X_analytic = []
for time in t:
    V_analytic.append(v_analytic(time))
    X_analytic.append((x_analytic(time)))

plt.subplot(2, 1, 1)
plt.plot(T, V, 'o', label='Numerical')
plt.plot(t, V_analytic, label='Analytic')
plt.title('Velocity vs Time Modified Eulers')
plt.xlabel('Time')
plt.ylabel('Velocity')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(X, Y[:, 0], 'o', label='Numerical')
plt.plot(t, X_analytic, label='Analytic')
plt.title('Position vs Time Modified Eulers')
plt.xlabel('Time')
plt.ylabel('Position')
plt.legend()
plt.grid(True)

plt.show()


