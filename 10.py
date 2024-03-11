import numpy as np
a = int(input("parte real: "))
b = int(input("parte imaginária: "))

r=(a**2 +b**2)**(0.5)
t=np.arctan(b/a)

print("magnitude: ",r)
print("fase",t)

