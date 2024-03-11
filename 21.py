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

rows1 = int(input("Digite o número de linhas da primeira matriz: "))
cols1 = int(input("Digite o número de colunas da primeira matriz: "))
rows2 = int(input("Digite o número de linhas da segunda matriz: "))
cols2 = int(input("Digite o número de colunas da segunda matriz: "))

matriz1 = criar_matriz(rows1, cols1)
matriz2 = criar_matriz(rows2, cols2)

resultado = np.kron(matriz1, matriz2)
print(resultado)