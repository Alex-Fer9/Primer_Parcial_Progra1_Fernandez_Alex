def invertir_matriz(matriz: list[list]) -> list[list]: #1
    matriz_nueva = []

    for c in range(len(matriz[0])):
        lista = []
        for f in range(len(matriz)):
            lista.append(matriz[f][c])
        matriz_nueva.append(lista)

    return matriz_nueva

def sumar_fila(matriz: list[list], fila_referencia: int) -> int: #2
    resultado = 0

    for columna in matriz[fila_referencia]:
        resultado += columna

    return resultado 
    
def buscar_minimo(matriz: list[list], fila_referencia: int) -> int:
    bandera = True
    for columna in matriz[fila_referencia]:
        if bandera == True or columna < minimo:
            minimo = columna
            bandera == False

    return minimo

def buscar_maximo(matriz: list[list], fila_referencia: int) -> int:
    bandera = True
    for columna in matriz[fila_referencia]:
        if bandera == True or columna > maximo:
            maximo = columna
            bandera == False

    return maximo

def filtrar_por_numero(matriz:list[list], fila_referencia: int, filtro: int) -> list[list]:
    lista_indices = []
    matriz_filtrada = []

    for f in range(len(matriz)):
        lista_info = []
        for c in range(len(matriz[f])):
            if filtro == c:
                lista_info.append(matriz[f][c])
        
        matriz_filtrada.append(lista_info)
    
    return matriz_filtrada

def calcular_recaudacion(matriz: list[list]) -> list[list]:
    matriz = remover_fila(4)
    
    for f in range(len(matriz)):
        lista_recadacion = []
        
        for unidad in matriz[2]:
            for precio in matriz[3]:
                recaudacion = unidad * precio
        lista_recadacion.append(recaudacion)

    matriz.append(lista_recadacion)

    return matriz
        

    

def remover_fila(matriz: list[list], fila: int) -> list[list]:
    matriz.remove(fila)
    return matriz



    
