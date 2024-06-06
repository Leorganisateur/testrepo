import numpy as np
import matplotlib.pyplot as plt

def ratio_taille(x,y):
    return x**2 / (x+y)**2

def ratio_buste(x,y):
    return (x**1 / y) - 1

p = np.linspace(30, 46, 1000)
t = np.linspace(20, 30, 1000)
h = np.linspace(32, 40, 1000)

fig, axes = plt.subplots()

# plt.plot(p, ratio_buste(p, 34))
# plt.plot(p, np.sqrt(ratio_buste(p, 34)))
axes.plot(h, (34**2 / 23**2) + ratio_buste(34, h) + ratio_taille(h, 23), label='p = 34, t = 23')
axes.plot(t, (34**2 / t**2) + ratio_buste(34, 34) + ratio_taille(34, t), label = 'p = 34, h = 34')
axes.plot(p, (p**2 / 23**2) + ratio_buste(p, 34) + ratio_taille(34, 23), label = 'h = 34, t = 23')

fig.legend()
fig.show()