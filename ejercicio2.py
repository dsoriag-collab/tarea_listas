def ejercicio_t2():
    """
    T2 — Estadísticas de una lista de notas   (Taller, Medio)
    -----------------------------------------------------------------
    Datos:  nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
            notas   = [ 8,     6,      10,      7,      5  ]
    Muestra: promedio, máxima, mínima, cantidad de aprobados (>= 7)
             y el nombre del mejor estudiante.
    ✋ MANUAL : un solo for con acumulador, campeón y contador.
    🐍 PYTHON : sum, max, min, len, notas.index(max(notas)) y
               aprobados con COMPRENSIÓN: [n for n in notas if n >= 7]
    Salida esperada: Promedio 7.20 · Máx 10 (Diana) · Mín 5 · Aprobados 3 de 5
    """
    print("T2 — Estadísticas de una lista de notas")
    estudiantes = ["Ana", "Luis", "Diana", "Beto", "Elena"]
    calificaciones = [8, 6, 10, 7, 5]

    suma_total = 0
    nota_alta = calificaciones[0]
    nota_baja = calificaciones[0]
    estudiante_top = estudiantes[0]
    cont_aprobados = 0
    cont_total = 0
    for pos in range(len(calificaciones)):
        valor = calificaciones[pos]
        suma_total = suma_total + valor
        cont_total = cont_total + 1
        if valor > nota_alta:
            nota_alta = valor
            estudiante_top = estudiantes[pos]
        if valor < nota_baja:
            nota_baja = valor
        if valor >= 7:
            cont_aprobados = cont_aprobados + 1
    media = suma_total / cont_total
    print(
        f"[Método manual] Media {media:.2f} | Nota más alta {nota_alta} ({estudiante_top}) | Nota más baja {nota_baja} | Aprobaron {cont_aprobados} de {cont_total}"
    )

    media = sum(calificaciones) / len(calificaciones)
    nota_alta = max(calificaciones)
    nota_baja = min(calificaciones)
    estudiante_top = estudiantes[calificaciones.index(max(calificaciones))]
    lista_aprobados = [c for c in calificaciones if c >= 7]
    print(
        f"[Método Python] Media {media:.2f} | Nota más alta {nota_alta} ({estudiante_top}) | Nota más baja {nota_baja} | Aprobaron {len(lista_aprobados)} de {len(calificaciones)}"
    )


if __name__ == "__main__":
    ejercicio_t2()
