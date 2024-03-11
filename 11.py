import matplotlib.pyplot as plt
import numpy as np


a = int(input("parte real: "))
b = int(input("parte imaginária: "))


plt.figure(figsize=(8, 6))
plt.plot([0, a], [0, b], 'b', label='Z')
plt.plot([0, a*a], [0, a*b], 'g', label='ZxR_0')
plt.plot([0, a*b], [0, b*b], 'g', label='ZxI_0')

plt.scatter([a, a*a, a*b], [b, a*b, b*b], color='red', marker='o')  
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.title('Questão 11')
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()
