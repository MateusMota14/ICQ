a = int(input("parte real 1 num: "))
b = int(input("parte imaginária 1 num: "))
c = int(input("parte real 2 num: "))
d = int(input("parte imaginária 2 num: "))

def multiplica(x, y, z, w):
    m = x*z-y*w
    n = x*w+y*z
    return m, n

def soma(x, y, z, w):
    r = x+z
    i = y+w
    return r, i

def conjugado(x,y):
    return x,y*(-1)

def somaConjugado(x,y,z,w):
    g=soma(conjugado(x,y)[0],conjugado(x,y)[1],conjugado(z,w)[0],conjugado(z,w)[1])
    h=conjugado(soma(x,y,z,w)[0],soma(x,y,z,w)[1])
    if g==h:
        print("conjugado da soma é a soma do conjugado")
    else:
        print("conjugado da soma não é a soma do conjugado")

def produtoConjugado(x,y,z,w):
    g=multiplica(conjugado(x,y)[0],conjugado(x,y)[1],conjugado(z,w)[0],conjugado(z,w)[1])
    h=conjugado(multiplica(x,y,z,w)[0],multiplica(x,y,z,w)[1])
    if g==h:
        print("conjugado da produto é o produto do conjugado")
    else:
        print("conjugado do produto não é o produto do conjugado")

somaConjugado(a,b,c,d)
produtoConjugado(a,b,c,d)