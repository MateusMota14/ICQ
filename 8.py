import matplotlib.pyplot as plt
import numpy as np

z1 = 2 -1j
z2 = 1 + 1j

soma = z1 + z2
subtracao = z1 - z2

parte_real_soma = [0, z1.real, soma.real]
parte_imaginaria_soma = [0, z1.imag, soma.imag]


parte_real_subtracao = [0, z1.real, subtracao.real]
parte_imaginaria_subtracao = [0, z1.imag, subtracao.imag]


plt.figure(figsize=(8, 6))
plt.plot([0, z1.real], [0, z1.imag], 'b', label='z1')
plt.plot([0, z2.real], [0, z2.imag], 'g', label='z2')
plt.plot(parte_real_soma, parte_imaginaria_soma, 'r--', label='Soma')
plt.plot(parte_real_subtracao, parte_imaginaria_subtracao, 'm--', label='Subtração')

plt.scatter([z1.real, z2.real, soma.real, subtracao.real], [z1.imag, z2.imag, soma.imag, subtracao.imag], color='red')
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.title('Soma e Subtração de Números Complexos')
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()