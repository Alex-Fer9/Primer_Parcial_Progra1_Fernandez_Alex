def validar_int(min: int, max: int) -> int:
    opcion = input(f"elija una opcion entre {min} y {max}: ")

    if not opcion or not opcion.isdigit() or not (min < opcion < max):
        print("error")
        return validar_int(min, max)
    
    return opcion