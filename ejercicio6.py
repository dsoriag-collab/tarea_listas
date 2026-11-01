def ejercicio_p3():
    """
    P3 — Números únicos manteniendo el orden
    Datos: [1, 3, 2, 3, 4, 1, 5, 2]
    ✋ MANUAL : recorrer y añadir si "not in unicos".
    🐍 PYTHON : list(dict.fromkeys(nums))   (y explica por qué list(set(nums))
               NO garantiza el orden)
    Salida esperada: [1, 3, 2, 4, 5]
    """
    print("P3 — Elementos únicos conservando el orden original")
    valores = [1, 3, 2, 3, 4, 1, 5, 2]
    distintos = []
    for valor in valores:
        if valor not in distintos:
            distintos.append(valor)
    print("MANUAL:", distintos)
    print("PYTHON:", list(dict.fromkeys(valores)))
    print("dict.fromkeys mantiene el orden de la primera aparición.")
    print(
        "list(set(valores)) no asegura ese orden porque un conjunto no respeta el orden de inserción."
    )


if __name__ == "__main__":
    ejercicio_p3()
