import numpy as np

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

def dagger(matriz):
    transposta = np.transpose(matriz)
    dagger = np.conjugate(transposta)
    return dagger

def produto_interno(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        print("Erro: As dimensões das matrizes não são compatíveis para o produto interno.")
        return None

    matriz1_np = np.array(matriz1)
    matriz2_np = np.array(matriz2)

    produto = np.dot(matriz1_np, matriz2_np)

    return produto

rows = int(input("Digite o número de linhas da matriz: "))
cols = int(input("Digite o número de colunas da matriz: "))

matriz = criar_matriz(rows, cols)

def identidade(matriz):
    for i in range(rows):
        for j in range(cols):
            if (i==j and matriz[i][j]!=1):
                return False
                
            elif(i!=j and matriz[i][j]!=0):
                return False
            else:
                return True

def comutatividade(matriz,dagger,produto_interno):
    if np.array_equal(produto_interno(matriz, dagger(matriz)),produto_interno(dagger(matriz),matriz)):
        return True
    else:
        return False
    
condicao1 = comutatividade(matriz,dagger,produto_interno)
condicao2 = identidade(matriz)

if(condicao1 & condicao2):
    print("é unitária")
else:
    print("não é unitária")

