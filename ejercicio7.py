def ejercicio_p4():
    """
    P4 — Segundo mayor (sin ordenar toda la lista)
    Datos: [5, 2, 9, 7, 9, 3, 8]
    ✋ MANUAL : dos campeones (mayor y segundo) en un solo recorrido.
    🐍 PYTHON (para comprobar): sorted(set(nums))[-2]
    Salida esperada: Mayor 9 · Segundo 8
    """
    print("P4 — Segundo mayor (sin ordenar toda la lista)")
    valores = [5, 2, 9, 7, 9, 3, 8]
    primero = None
    segundo_lugar = None
    for dato in valores:
        if primero is None or dato > primero:
            segundo_lugar = primero
            primero = dato
        elif dato != primero and (segundo_lugar is None or dato > segundo_lugar):
            segundo_lugar = dato
    if segundo_lugar is None:
        print("La lista no contiene dos valores diferentes")
    else:
        print(
            f"[Manual] Valor más grande: {primero} | Segundo más grande: {segundo_lugar}"
        )
    print(
        f"[Python] Valor más grande: {max(valores)} | Segundo más grande: {sorted(set(valores))[-2]}"
    )


if __name__ == "__main__":
    ejercicio_p4()
