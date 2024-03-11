import numpy as np


def transposta(matriz):
    transposta = np.transpose(matriz)
    return transposta


def conjugada(matriz):
    conjugada = np.conjugate(matriz)
    return conjugada

def criar_matriz(rows, cols):
    matriz = []
    for i in range(rows):
        linha = []
        for j in range(cols):
            parte_real = float(
                input(f"Digite a parte real do elemento ({i+1}, {j+1}): "))
            parte_imaginaria = float(
                input(f"Digite a parte imaginária do elemento ({i+1}, {j+1}): "))
            numero_complexo = complex(parte_real, parte_imaginaria)
            linha.append(numero_complexo)
        matriz.append(linha)
    return matriz


n_linhas = int(input("Digite o número de linhas da matriz: "))
n_colunas = int(input("Digite o número de colunas da matriz: "))

matriz = criar_matriz(n_linhas, n_colunas)

if np.array_equal(transposta(matriz), conjugada(matriz)):
    print("matriz é hermitiana")
else:
    print("matriz não é hermitiana")

