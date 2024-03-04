print("parte real do primeiro número")
a = int(input())
print("parte imaginária do primeiro número")
b = int(input())
print("parte real do segundo número")
c = int(input())
print("parte imaginária do segundo número")
d = int(input())

def soma(x,y,z,w):
    f= x+z
    g = y+w
    if g < 0 :
        e=f"{f}{g}i"
    else :
        e=f"{f}+{g}i"
    print("a soma é:",e)

def multiplica(x,y,z,w):
    h=x*z-y*w
    i=x*w+y*z
    if i<0:
        j=f"{h}{i}i"
    else:
        j=f"{h}+{i}i"
    print("o produto é:",j)

soma(a,b,c,d)
multiplica(a,b,c,d)