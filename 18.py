import numpy as np

def criar_matriz(rows, cols):
    matriz = []
    for i in range(rows):
        linha = []
        for j in range(cols):
            parte_real = float(input(f"Digite a parte real do elemento ({i+1}, {j+1}): "))
            parte_imaginaria = float(input(f"Digite a parte imaginária do elemento ({i+1}, {j+1}): "))
            numero_complexo = complex(parte_real, parte_imaginaria)
            linha.append(numero_complexo)
        matriz.append(linha)
    return matriz

rows = int(input("Digite o número de linhas da primeira matriz: "))
cols = int(input("Digite o número de colunas da primeira matriz: "))

matriz = criar_matriz(rows, cols)

traco=0
for i in range(rows):
    for j in range(cols):
        if(i==j):
            traco+=matriz[i][j]

print(traco)