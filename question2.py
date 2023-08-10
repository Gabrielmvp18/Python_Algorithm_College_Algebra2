def multiplicar_matrizes(A, B):
    
    A_linhas = len(A)
    
    A_colunas = len(A[0])
    
    B_linhas = len(B)
    
    B_colunas = len(B[0])
    
    # Verifiquei se as matrizes podem ser multiplicadas
    if (A_colunas != B_linhas):
        return "Não é possível multiplicar essas matrizes!"
    
    # Criando matriz resultado com os elementos sendo zeros
    resultado = []
    for i in range(A_linhas):
        linha = []
        for j in range(B_colunas):
            linha.append(0)
        resultado.append(linha)
    
    # Calculando multiplicação
    for i in range(A_linhas): # esse for irá percorrer cada linha da Matriz A
        for j in range(B_colunas): # esse for irá percorrer cada coluna da Matriz B
            soma = 0 # Criei a variavel soma aqui porque ela armazenará os elementos que selecionei com os dois for acima das respectivas matrizes 
            for k in range(A_colunas): #Esse percorre cada coluna de A que é igual a linha de B, multiplicando o elementos e soma-los.
                soma += A[i][k] * B[k][j]
            resultado[i][j] = soma
            
            #Esse processo se repete para todos os elementos da matriz resultado, devido aos dois primeiros loops (loops i e j).
    
    return resultado

# Aqui eu coloquei a Matriz dada no desafio que representa os estilos
estilos = [
    [5, 20, 16, 7, 17],
    [7, 18, 12, 9, 21],
    [6, 25, 8, 5, 13]
]

# Aqui eu coloquei a Matriz dada no desafio que é são os preços 
precos = [
    [15, 9, 13],
    [8, 7, 10],
    [5, 7, 2],
    [1, 5, 1],
    [10, 11, 11]
]

orcamento = multiplicar_matrizes(estilos, precos)

#aqui eu fiz uma simples repetição para imprimir 3 vezes os valores, o i começa em 0 e vai até o 2 que corresponde ao estilo e o segundo indice 0,1,2 corresponde a loja. 
for i in range(3):
    print(f"Estilo E{i+1} - L1: {orcamento[i][0]*100} reais, L2: {orcamento[i][1]*100} reais, L3: {orcamento[i][2]*100} reais")
