import matplotlib.pyplot as plt
import numpy as np

z1 = 2 - 1j
z2 = 1 + 1j

soma = z1 + z2
subtracao = z1 - z2

r1, theta1 = np.abs(z1), np.angle(z1)
r2, theta2 = np.abs(z2), np.angle(z2)
r_soma, theta_soma = np.abs(soma), np.angle(soma)
r_subtracao, theta_subtracao = np.abs(subtracao), np.angle(subtracao)

plt.figure(figsize=(8, 6))
plt.polar([0, theta1], [0, r1], label='z1', marker='o')
plt.polar([0, theta2], [0, r2], label='z2', marker='o')
plt.polar([0, theta_soma], [0, r_soma], 'r--', label='Soma')
plt.polar([0, theta_subtracao], [0, r_subtracao], 'm--', label='Subtração')

plt.title('Soma e Subtração de Números Complexos (Forma Polar)')
plt.legend()
plt.show()