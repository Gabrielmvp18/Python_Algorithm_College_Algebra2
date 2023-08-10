# Esta função irá calcular o custo total de cada modelo. 

def custo_total(fabrica1, fabrica2):
    resultado = []  #Aqui temos uma lista vazia que irei armazenas os custos somados para ter o resultado total.
    
    for i in range(len(fabrica1)):  # Utilizei um loop (for) para eu iterar em cada item e assim conseguir fazer a soma e ter o resultado do custo total por modelo
        
        soma_total = fabrica1[i][0] + fabrica1[i][1] + fabrica2[i][0] + fabrica2[i][1]
        resultado.append(soma_total)
        
    return resultado

# Estas são as matrizes de custo para ambas as fábricas
F1 = [
    [32, 40],  
    [50, 80],  
    [70, 20]   
]

F2 = [
    [40, 60],  
    [50, 50],  
    [130, 20]  
]

custos = custo_total(F1, F2) 

print(f"Modelo A: {custos[0]} reais")
print(f"Modelo B: {custos[1]} reais")
print(f"Modelo C: {custos[2]} reais")
