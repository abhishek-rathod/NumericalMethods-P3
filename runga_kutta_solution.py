"""
This moduel contains the solution using rk4 method
it imports the functions from the methods.py module
"""

from methods import *

'''
Using rk4 to solve for velocity as a function of time
'''
t = 0.0
tstop = 10.0
v = 0.0
h = 0.1
T, V = rungakutta4(f, t, v, tstop, h)


'''
Now using rk4 to solve for position
y is position here and x is time
'''

x = 0.0
xstop = 10.0
y = np.array([0.0, 0.0]) #array of initial condions y_naught and yprime_naught
X, Y = rungakutta4(F, x, y, xstop, h)

t = np.linspace(0, 10, 100)
V_analytic = []
X_analytic = []
for time in t:
    V_analytic.append(v_analytic(time))
    X_analytic.append((x_analytic(time)))



plt.subplot(2, 1, 1)
plt.plot(T, V, 'o')
plt.plot(t, V_analytic)
plt.title('Velocity vs Time RK4')
plt.xlabel('Time')
plt.ylabel('Velocity')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(X, Y[:, 0],'o')
plt.plot(t, X_analytic)
plt.title('Position vs Time RK4')
plt.xlabel('Time')
plt.ylabel('Position')
plt.grid(True)

plt.show()

