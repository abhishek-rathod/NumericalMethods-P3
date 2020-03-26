import numpy as np
import matplotlib.pyplot as plt
import math

def rk4(f, a, b, h, yo):
    n = math.ceil((b - a) / h)
    sols = np.zeros((n+1, 2))
    fs = np.zeros((n+1, 4))
    sols[0, 1] = yo
    sols[0, 0] = a
    for i in range(n):
        k = i + 1
        fs[i, 0] = f(sols[i, 0], sols[i, 1])
        fs[i, 1] = f(sols[i, 0] + h / 2, sols[i, 1] + (h / 2) * fs[i, 0])
        fs[i, 2] = f(sols[i, 0] + h / 2, sols[i, 1] + (h / 2) * fs[i, 1])
        fs[i, 3] = f(sols[i, 0] + h, sols[i, 1] + h * fs[i, 2])
        sols[k, 0] = sols[i, 0] + h
        sols[k, 1] = sols[i, 1] + (h / 6) * (fs[i, 0] + 2*fs[i, 1] + 2*fs[i, 2] + fs[i, 3])

    return sols

def modified_eulers(f, yo, h, a, b):
    '''

    this function takes the parameters described below, and
    builds a table in which the first column is the xn
    the second column is xmid, third column is

    :param f: the function
    :param yo: initial condition
    :param h: step size
    :param a: lower bound
    :param b: upper bound
    :return: complete n+1 by 5 table described above
    '''

    n = math.ceil((b-a)/h)
    table = np.zeros((n+1, 5))
    table[0, 2] = yo
    for i in range(n):
        k = i+1
        table[i, 0] = a + i*h
        table[i, 1] = table[i, 0] + h/2
        table[i, 3] = f(table[i, 0], table[i, 2])
        table[i, 4] = table[i, 2] + table[i, 3]*h/2
        table[k, 2] = table[i, 2] + h*f(table[i, 1], table[i, 4])
    table[n, 0] = n*h
    return table

def f(t, v):
    g = 9.8
    k = 10**-4
    m = 10**-2
    return g - (k/m)*(v**2)

def F(t, y):
    g = 9.8
    k = 10 ** -4
    m = 10 ** -2
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = g - (k/m)*(y[1]**2)

    return F


def rungakutta4(f, x, y, xstop, h):


    def rk4(f, x, y, h):
        K0 = h*f(x, y)
        K1 = h*f(x + h/2.0, y + K0/2.0)
        K2 = h*f(x + h/2.0, y + K1/2.0)
        K3 = h*f(x + h, y + K2)
        return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0

    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xstop:
        h = min(h, xstop - x)
        y = y + rk4(f, x, y, h)
        x = x + h
        X.append(x)
        Y.append(y)
    return np.array(X), np.array(Y)

