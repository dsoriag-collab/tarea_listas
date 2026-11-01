def ejercicio_t1():
    """
    T1 — CRUD de pasajeros con clase Pasajero + list   (Taller, Medio)
    -----------------------------------------------------------------
    Demuestra (sin menú, con llamadas directas) el CRUD completo usando
    tu clase ListaPasajerosPython:
        añadir 3 pasajeros -> listar -> buscar por cédula -> modificar
        -> eliminar -> listar otra vez -> ordenar por NOMBRE con
        sort(key=lambda p: p.nombre)  (es el reto del taller).
    Importa así:  from lista_python import ListaPasajerosPython
                  from pasajero import Pasajero
    """
    print('T1 — CRUD de pasajeros con clase Pasajero + list')
    from lista_python import ListaPasajerosPython
    from pasajero import Pasajero

    registro = ListaPasajerosPython()
    registro.añadir(Pasajero("Valeria", "0931234567", 24))
    registro.añadir(Pasajero("Andrés", "0945678123", 30))
    registro.añadir(Pasajero("Mateo", "0956789012", 41))
    print("=== Registro inicial de pasajeros ===")
    registro.listar()

    cedula_buscada = "0945678123"
    indice = registro.buscar(cedula_buscada)
    if indice == -1:
        print("La cédula buscada no está registrada")
    else:
        print(f"Pasajero localizado en la posición [{indice}]: {registro.pasajeros[indice]}")

    if registro.modificar("0956789012", "Sebastián", 42):
        print("✔ Los datos del pasajero fueron actualizados")
    if registro.eliminar_por_valor("0945678123"):
        print("✔ El pasajero fue removido de la lista")
    print("=== Registro tras actualizar y remover ===")
    registro.listar()

    registro.pasajeros.sort(key=lambda p: p.nombre)
    print("=== Registro ordenado alfabéticamente por nombre ===")
    registro.listar()


if __name__ == "__main__":
    ejercicio_t1()