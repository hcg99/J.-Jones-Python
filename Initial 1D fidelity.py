import numpy as np
import matplotlib.pyplot as plt
import math



def naive_NOT_0(e):
    F = 1 - (e**2 * math.pi**2)/8
    return F

def naive_NOT_1(e):
    F = np.array([])
    for i in range(len(e)):
        F = np.append(F, math.cos(e[i]*math.pi/2))
    return F

def n_equals_3_NOT(e):
    F = 1 - (3 * e**4 * math.pi**4)/128
    index_remove = []
    for i in range(len(F)):
        if F[i] < 0:
            index_remove.append(i)
    print(F)
    F = np.delete(F, index_remove)
    print(F)
    e = np.delete(e, index_remove)
    return F, e

e = np.linspace(-1, 1, 500)
F0 = naive_NOT_0(e)
F1 = naive_NOT_1(e)
F_n3, e_n3 = n_equals_3_NOT(e)

#plt.plot(e, F0)
plt.plot(e, F1, label='naive')
plt.plot(e_n3, F_n3, label='n=3 equilateral triangle')
plt.xlabel('pulse strength error')
plt.ylabel('fidelity')
plt.title('Fidelity as a function of pulse strength error')
plt.legend()
plt.show()


plt.plot(e, 1 - F1, label='naive')
plt.plot(e_n3, 1 - F_n3, label='n=3 equilateral triangle')
#plt.yscale('log')
#plt.plot(e, F1)
plt.xlabel('pulse strength error')
plt.ylabel('fidelity')
plt.title('Inidelity as a function of pulse strength error')
#plt.legend()
plt.show()
