a = int(input("parte real 1 num: "))
b = int(input("parte imaginária 1 num: "))
c = int(input("parte real 2 num: "))
d = int(input("parte imaginária 2 num: "))
e = int(input("parte real 3 num: "))
f = int(input("parte imaginária 3 num: "))


def soma(x, y, z, w):
    r = x+z
    i = y+w
    return r, i


def multiplica(x, y, z, w):
    m = x*z-y*w
    n = x*w+y*z
    return m, n

def comutatividadeSoma(x,y,w,z):
    if soma(x,y,w,z)==soma(w,z,x,y):
        print("comutativo na soma")
    else:
        print("não é comutativo na soma")

def comutatividadeMultiplica(x,y,w,z):
    if multiplica(x,y,w,z)==multiplica(w,z,x,y):
        print("comutativo na multiplicação")
    else:
        print("não é comutativo na multiplicação")


def assossiatividadeSoma(x, y, z, w, u, v):
    g = soma(soma(x, y, z, w)[0], soma(x, y, z,w)[1], u, v)
    h = soma(x, y, soma(z, w, u, v)[0], soma(z,w,u,v)[1])
    if g == h:
        print("assossiativo na soma")
    else:
        print("não é assossiativo na soma")


def assossiatividadeMultiplica(x, y, z, w, u, v):
    g = multiplica(multiplica(x, y,z,w)[0], multiplica(x, y, z,w)[1], u, v)
    h = multiplica(x, y, multiplica(z, w, u, v)[0], multiplica(z,w,u,v)[1])
    if g == h:
        print("assossiativo na multiplicação")
    else:
        print("não é assossiativo na multiplicação")

def distributividade(x,y,z,w,u,v):
    g=multiplica(x,y,soma(z,w,u,v)[0],soma(z,w,u,v)[1])
    h=soma(multiplica(x,y,z,w)[0],multiplica(x,y,z,w)[1],multiplica(x,y,u,v)[0],multiplica(x,y,u,v)[1])
    if g==h:
        print("distributivo")
    else:
        print("não é distributivo")

comutatividadeSoma(a,b,c,d)
comutatividadeMultiplica(a,b,c,d)
assossiatividadeSoma(a, b, c, d, e, f)
assossiatividadeMultiplica(a,b,c,d,e,f)
distributividade(a,b,c,d,e,f)
