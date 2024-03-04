a = int(input("parte real 1 num: "))
b = int(input("parte imaginária 1 num: "))
c = int(input("parte real 2 num: "))
d = int(input("parte imaginária 2 num: "))

def multiplica(x, y, z, w):
    m = x*z-y*w
    n = x*w+y*z
    return m, n
def modulo(x,y):
    return (x**2 + y**2)**0.5

def soma(x, y, z, w):
    r = x+z
    i = y+w
    return r, i

def checagem(x,y,z,w):
    g=multiplica(modulo(x,y),0,modulo(z,w),0)[0]
    h=modulo(multiplica(x,y,z,w)[0],multiplica(x,y,z,w)[1])
    if g==h:
        print("produto dos módulos é o módulo do produto")
    else:
        print("produto dos módulos não é o módulo do produto")

def desigualdade(x,y,z,w):
    g=modulo(soma(x,y,z,w)[0],soma(x,y,z,w)[1])
    h=soma(modulo(x,y),0,modulo(z,w),0)[0]
    print(g)
    print(h)
    if g>h:
        print("desigualdade inválida")
    else:
        print("desigualdade é válida")
checagem(a,b,c,d)
desigualdade(a,b,c,d)