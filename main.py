from UTN_Heroes_Dataset.utn_pp import get_original_matrix
from UTN_Heroes_Dataset.utn_pp import mostrar_matriz_texto_tabla
from funciones import *
matriz_consesionaria = get_original_matrix()

def PP_app(matriz):
    opcion = validar_int(1, 9)

    while True:
        mostrar_menu()

        match opcion:
            case 1:
                PP_mostrar_existencia(matriz)
            case 2:
                PP_mostrar_cantidad_unidades(matriz)
            case 3:
                PP_mostrar_garaje_menos_veiculos(matriz)
            case 4:
                PP_mostrar_maxima_cantidad(matriz)
            case 5:
                PP_obtener_recaudacion(matriz)
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                break

PP_app(matriz_consesionaria)