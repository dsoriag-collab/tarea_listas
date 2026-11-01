def ejercicio_p2():
    """
    P2 — Invertir una lista SIN lista.reverse()
    Datos: [1, 2, 3, 4, 5]
    ✋ MANUAL : for con range(len(lista)-1, -1, -1) y append.
    🐍 PYTHON : lista[::-1]  y  list(reversed(lista))
    🧩 COMPRENSIÓN: [lista[i] for i in range(len(lista)-1, -1, -1)]
    Salida esperada: [5, 4, 3, 2, 1]
    """
    print("P2 — Invertir una lista SIN lista.reverse()")
    secuencia = [1, 2, 3, 4, 5]
    al_reves = []
    for k in range(len(secuencia) - 1, -1, -1):
        al_reves.append(secuencia[k])
    print("[Manual] Lista invertida:", al_reves)
    print("[Python con slicing] Lista invertida:", secuencia[::-1])
    print("[Python con reversed] Lista invertida:", list(reversed(secuencia)))
    al_reves = [secuencia[k] for k in range(len(secuencia) - 1, -1, -1)]
    print("[Comprensión] Lista invertida:", al_reves)


if __name__ == "__main__":
    ejercicio_p2()
