import numpy as np
import matplotlib.pyplot as plt
import math


def f(t, v):
    '''

    :param t: time
    :param v: velocity
    :return: the function stated in the problem
    '''
    g = 9.8
    k = 10**-4
    m = 10**-2
    return g - (k/m)*(v**2)


def F(t, y):
    '''

    :param t: time
    :param y: position
    :return: the function stated in the problem, but written as
    two first order DEs
    '''
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


def modified_eulers(f, x, y, xstop, h):

    X = []
    Y = []
    X.append(x)
    Y.append(y)
    while x < xstop:
        xmid = x + h/2
        ymid = y + h/2
        y = y + h*f(xmid, ymid)
        x = x + h
        X.append(x)
        Y.append(y)
    return np.array(X), np.array(Y)
