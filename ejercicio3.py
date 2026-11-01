def ejercicio_t3():
    """
    T3 — Ordenar una lista (bubble sort)   (Taller, Avanzado)
    -----------------------------------------------------------------
    Datos: [5, 2, 8, 1, 9, 3, 7]
    ✋ MANUAL : burbuja con bandera hubo_swap (sobre una COPIA lista[:]).
    🐍 PYTHON : sorted(lista) y lista.sort(reverse=True).
    Extra    : palabras = ["python", "a", "código", "el"] ordenadas con key=len
    Salida esperada: [1, 2, 3, 5, 7, 8, 9]
    """
    print("T3 — Ordenamiento de una lista mediante bubble sort")
    numeros = [5, 2, 8, 1, 9, 3, 7]
    arreglo = numeros[:]
    for pasada in range(len(arreglo) - 1):
        intercambio = False
        for i in range(len(arreglo) - 1 - pasada):
            if arreglo[i] > arreglo[i + 1]:
                temp = arreglo[i]
                arreglo[i] = arreglo[i + 1]
                arreglo[i + 1] = temp
                intercambio = True
        if not intercambio:
            break
    print("MANUAL:", arreglo)
    print("Original:", numeros)
    print("PYTHON ascendente:", sorted(numeros))
    numeros.sort(reverse=True)
    print("PYTHON descendente:", numeros)

    terminos = ["python", "a", "código", "el"]
    terminos.sort(key=len)
    print("Palabras por longitud:", terminos)


if __name__ == "__main__":
    ejercicio_t3()
