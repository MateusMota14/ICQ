a = int(input("parte real: "))
b = int(input("parte imaginária: "))

def inversa(x, y):
    c=x**2+y**2
    return x/c, -y/c
e=inversa(a,b)[1]
f=inversa(a,b)[0]
print(f,e)