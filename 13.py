import numpy as np
import matplotlib.pyplot as plt

a = int(input("parte real: "))
b = int(input("parte imaginária: "))

def soma_imag(x, y, n):
    c = y
    for i in range(n):
        y += c
    return x, y

somas_complexas = []

for i in range(1, 11):
    parte_real, parte_imag = soma_imag(a, b, i)
    somas_complexas.append(complex(parte_real, parte_imag))

partes_reais = [np.real(z) for z in somas_complexas]
partes_imaginarias = [np.imag(z) for z in somas_complexas]

plt.scatter(partes_reais, partes_imaginarias, label='Somas da parte imaginária')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.title('Valores após soma da parte imaginária')
plt.legend()
plt.grid(True)
plt.show()
