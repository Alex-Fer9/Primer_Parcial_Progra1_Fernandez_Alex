from UTN_Heroes_Dataset.utn_pp import get_original_matrix
from UTN_Heroes_Dataset.utn_pp import mostrar_matriz_texto_tabla
matriz_consesionaria = get_original_matrix()

def invertir_matriz(matriz: list[list]) -> list[list]:
    matriz_nueva = []

    for c in range(len(matriz[0])):
        lista = []
        for f in range(len(matriz)):
            lista.append(matriz[f][c])
        matriz_nueva.append(lista)

    return matriz_nueva

def PP_mostrar_existencia(matriz):
    nombres_info = ["marca", "modelo", "unidades", "recaudación", ""]
    matriz_mostrar = invertir_matriz(matriz)
    
    mostrar_matriz_texto_tabla(matriz_mostrar, nombres_info)


if __name__ == "__main__":
    from UTN_Heroes_Dataset.utn_pp import get_original_matrix
    from UTN_Heroes_Dataset.utn_pp import mostrar_matriz_texto_tabla
    matriz_consesionaria = get_original_matrix()

    PP_mostrar_existencia(matriz_consesionaria)

# def sumar_fila(matriz: list[list], fila_referencia: int) -> int:
#     resultado = 0

#     for columna in matriz[fila_referencia]:
#         resultado += columna

#     return resultado 

# print(sumar_fila(matriz_consesionaria, 2))

def buscar_minimo(matriz: list[list], fila_referencia: int) -> int:
    bandera = True
    for columna in matriz[fila_referencia]:
        if bandera == True or columna < minimo:
            minimo = columna
            bandera = False

    return minimo

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

def PP_mostrar_garaje_menos_veiculos(matriz):
    unidad_minima = buscar_minimo(matriz, 2)
    print(unidad_minima)
    matriz_filtrada = filtrar_por_numero(matriz, 2, unidad_minima)

    PP_mostrar_existencia(matriz_filtrada)

PP_mostrar_garaje_menos_veiculos(matriz_consesionaria)