import numpy as np
import matplotlib.pyplot as plt

a = int(input("parte real: "))
b = int(input("parte imaginária: "))

def multiplica(x, y, z, w):
    m = x*z - y*w
    n = x*w + y*z
    return m, n

def potencia(x, y, n, multiplica):
    if n == 1:
        return x, y
    elif 1 < n <= 10:
        c = x
        d = y
        for i in range(n-1):
            e = x
            x = multiplica(x, y, c, d)[0]
            y = multiplica(e, y, c, d)[1]
        return x, y

potencias_complexas = []

for i in range(1, 11):
    pot_real, pot_imag = potencia(a, b, i, multiplica)
    potencias_complexas.append(complex(pot_real, pot_imag))

partes_reais = [np.real(z) for z in potencias_complexas]
partes_imaginarias = [np.imag(z) for z in potencias_complexas]

plt.scatter(partes_reais, partes_imaginarias, label='Potências')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.title('Potências de um número complexo')
plt.legend()
plt.grid(True)
plt.show()
