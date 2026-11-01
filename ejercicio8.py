def ejercicio_p5():
    """
    P5 — Fusionar dos listas ordenadas (sin sort)
    Datos: a = [1, 3, 5, 7],  b = [2, 4, 6, 8, 10]
    ✋ MANUAL : dos índices i, j comparando cabezas (base del merge sort)
               y al final extend con lo que sobre.
    🐍 PYTHON (para comprobar): sorted(a + b)
    Salida esperada: [1, 2, 3, 4, 5, 6, 7, 8, 10]
    """
    print("P5 — Combinar dos listas ordenadas (sin usar sort)")
    lista1 = [1, 3, 5, 7]
    lista2 = [2, 4, 6, 8, 10]
    combinada = []
    indice1 = 0
    indice2 = 0
    while indice1 < len(lista1) and indice2 < len(lista2):
        if lista1[indice1] <= lista2[indice2]:
            combinada.append(lista1[indice1])
            indice1 = indice1 + 1
        else:
            combinada.append(lista2[indice2])
            indice2 = indice2 + 1
    combinada.extend(lista1[indice1:])
    combinada.extend(lista2[indice2:])
    print("BUCLE:", combinada)
    print("SORTED:", sorted(lista1 + lista2))


if __name__ == "__main__":
    ejercicio_p5()
