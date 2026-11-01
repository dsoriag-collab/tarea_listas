def ejercicio_p1():
    """
    P1 — Contar apariciones de un valor
    Datos: lista = [1, 3, 2, 3, 4, 3, 5],  v = 3
    ✋ MANUAL : patrón contador.   🐍 PYTHON : lista.count(v)
    🧩 COMPRENSIÓN: len([x for x in lista if x == v])
    Salida esperada: 3 aparece 3 veces
    """
    print("P1 — Contar apariciones de un valor")
    datos = [1, 3, 2, 3, 4, 3, 5]
    objetivo = 3
    repeticiones = 0
    for elemento in datos:
        if elemento == objetivo:
            repeticiones = repeticiones + 1
    print(f"[Manual] El número {objetivo} se repite {repeticiones} veces")
    print(f"[Python] El número {objetivo} se repite {datos.count(objetivo)} veces")
    repeticiones = len([e for e in datos if e == objetivo])
    print(f"[Comprensión] El número {objetivo} se repite {repeticiones} veces")


if __name__ == "__main__":
    ejercicio_p1()
