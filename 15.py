n = int(input("dimensão dos vetores: "))
a = int(input("parte real do escalar: "))
b = int(input("parte imaginária do escalar: "))
vetor1=[]
vetor2=[]
def soma(vetor1, vetor2):
    array_soma = []
    for i in range(len(vetor1)):
        array_soma.append(vetor1[i] + vetor2[i])
    return array_soma
def inversa(vetor):
    return [-x for x in vetor]
def escalar(vetor,c):
    return [c * x for x in vetor]

for i in range(n):
     r=int(input(f"parte real do elemento {i+1} do vetor 1: "))
     c=int(input(f"parte imaginária do elemento {i+1} do vetor 1: "))
     vetor1.append(complex(r, c))
     r=0
     c=0

for i in range(n):
     r=int(input(f"parte real do elemento {i+1} do vetor 2: "))
     c=int(input(f"parte imaginária do elemento {i+1} do vetor 2: "))
     vetor2.append(complex(r, c))
     r=0
     c=0

escalar_complexo=complex(a,b)
print("soma dos vetores:",soma(vetor1,vetor2))
print("inversa do vetor",inversa(vetor1))
print("multiplicação por escalar:",escalar(vetor1,escalar_complexo))
