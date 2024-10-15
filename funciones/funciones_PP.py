from .auxiliares import (invertir_matriz, sumar_fila, buscar_minimo, filtrar_por_numero, buscar_maximo, calcular_recaudacion)

def PP_mostrar_existencia(matriz):
    nombres_info = ["marca", "modelo", "unidades", "recaudación", ""]
    matriz_mostrar = invertir_matriz(matriz)
    
    mostrar_matriz_texto_tabla(matriz_mostrar, nombres_info)

def PP_mostrar_cantidad_unidades(matriz):
    total_unidades = sumar_fila(matriz, 2)

    print(f"la cantidad total de todos los veículos es {total_unidades}")

def PP_mostrar_garaje_menos_veiculos(matriz):
    unidad_minima = buscar_minimo(matriz, 2)
    matriz = filtrar_por_numero(matriz, 2, unidad_minima)

    PP_mostrar_existencia(matriz)

def PP_mostrar_maxima_cantidad(matriz):
    unidad_maxima = buscar_maximo(matriz, 2)

    print(f"EL garaje con mas unidades es {unidad_maxima}")

def PP_obtener_recaudacion(matriz):
    matriz_nueva = PP_obtener_recaudacion(matriz)

    PP_mostrar_existencia(matriz_nueva)




if __name__ == "__main__":
    from UTN_Heroes_Dataset.utn_pp import get_original_matrix
    from UTN_Heroes_Dataset.utn_pp import mostrar_matriz_texto_tabla
    matriz_consesionaria = get_original_matrix()

    PP_mostrar_existencia(matriz_consesionaria)
