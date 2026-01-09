def encontrar_maximo(lista: list | None):
    """
    Encuentra el valor máximo en una lista sin usar max().

    Reglas:
    - None -> None
    - No list -> TypeError
    - Lista vacía -> None
    - Lista con valores -> valor máximo
    """
    if lista is None:
        return None

    if not isinstance(lista, list):
        raise TypeError("El parámetro 'lista' debe ser una lista o None.")

    if len(lista) == 0:
        return None

    maximo = lista[0]

    for valor in lista[1:]:
        if valor > maximo:
            maximo = valor

    return maximo
