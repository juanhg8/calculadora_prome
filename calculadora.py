#!/usr/bin/env python3
"""Calculadora de promedios simple.

Este script se ejecuta en la terminal y permite ingresar el nombre de un
estudiante, la cantidad de materias, y luego solicitar el nombre y la
nota de cada materia. Al terminar, muestra el promedio final.

Uso:
    python calculadora.py
"""

def main():
    print("Calculadora de promedios\n")
    print("Nota mínima para pasar: 6.0\n")

    while True:  # repetir hasta que el usuario decida salir
        nombre = input("Ingrese el nombre del estudiante: ")

        # Validar número de materias
        while True:
            try:
                cantidad = int(input("¿Cuántas materias desea agregar? "))
                if cantidad <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Por favor ingrese un número entero positivo.")

        total = 0.0
        materias = []

        for i in range(1, cantidad + 1):
            materia = input(f"Nombre de la materia #{i}: ")
            while True:
                try:
                    nota = float(input(f"Nota para {materia}: "))
                    if nota < 0 or nota > 10:
                        raise ValueError
                    break
                except ValueError:
                    print("Por favor ingrese una nota válida (0-10).")

            materias.append((materia, nota))
            total += nota

        promedio = total / cantidad

        print("\n--- Resultado ---")
        print(f"Estudiante: {nombre}")
        for materia, nota in materias:
            print(f"  {materia}: {nota}")
        print(f"Promedio general: {promedio:.2f}")
        if promedio >= 6.0:
            print("Estado: APROBADO")
        else:
            print("Estado: REPROBADO")

        # preguntar si desea continuar
        seguir = input("\n¿Desea calcular otro estudiante? (s/n): ").strip().lower()
        if seguir != 's':
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break


if __name__ == "__main__":
    main()
