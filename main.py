"""
Actividad Práctica: Evaluación de la Ecuación de la Recta
Asignatura: Ciencia de Datos
Alumno: Gomez Estrada Esteban
Matrícula: 2403230186
Fecha: 21/Septiembre/2026
"""

from funciones import obtener_parametros, evaluar_funcion


funcion = ""
m = 0
b = 0
n = 0
funcion_capturada = False
muestras_capturadas = False


while True:

    print("\n========== MENU PRINCIPAL ==========")
    print("1. Capturar función lineal")
    print("2. Capturar número de muestras")
    print("3. Capturar valores de x y evaluar")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":

        try:
            funcion = input("\nEscribe la función lineal: ")

            m, b = obtener_parametros(funcion)

            funcion_capturada = True

            print("\nFunción capturada correctamente.")
            print("Pendiente (m):", m)
            print("Ordenada al origen (b):", b)

        except ValueError:
            print("\nError: escribe una función válida.")
            print("Ejemplos: 2x + 3, -1.5x - 4, x + 5")

    elif opcion == "2":

        try:
            n = int(input("\n¿Cuántas muestras deseas evaluar?: "))

            if n <= 0:
                print("El número de muestras debe ser mayor que 0.")
            else:
                muestras_capturadas = True
                print("Número de muestras:", n)

        except ValueError:
            print("Error: debes escribir un número entero.")

    elif opcion == "3":

        if not funcion_capturada:
            print("\nPrimero debes capturar una función.")

        elif not muestras_capturadas:
            print("\nPrimero debes capturar el número de muestras.")

        else:

            resultados = []

            print("\n========== RESULTADOS ==========")
            print("m =", m)
            print("b =", b)

            for i in range(n):

                try:
                    x = float(input("Ingresa x" + str(i + 1) + ": "))

                    y = evaluar_funcion(m, b, x)

                    resultados.append((x, y))

                except ValueError:
                    print("Valor no válido. Intenta nuevamente.")
                    continue

            print("\nTabla de resultados")
            print("-------------------------")
            print("   x       y")
            print("-------------------------")

            for x, y in resultados:
                print(" ", x, "   ", y)

    elif opcion == "4":

        print("\nPrograma terminado.")
        break

    else:

        print("\nOpción no válida. Selecciona del 1 al 4.")