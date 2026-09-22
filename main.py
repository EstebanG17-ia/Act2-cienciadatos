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

while True:

    print("\n========== MENU PRINCIPAL ==========")
    print("1. Capturar función lineal")
    print("2. Capturar número de muestras")
    print("3. Capturar valores de x y evaluar")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":

        funcion = input("\nEscribe la función lineal: ")

        m, b = obtener_parametros(funcion)

        print("\nFunción capturada correctamente.")
        print("Pendiente (m):", m)
        print("Ordenada al origen (b):", b)

    elif opcion == "2":

        n = int(input("\n¿Cuántas muestras deseas evaluar?: "))

        print("Número de muestras:", n)

    elif opcion == "3":

        print("\nCaptura los valores de x:")

        for i in range(n):

            x = float(input("x" + str(i + 1) + ": "))

            y = evaluar_funcion(m, b, x)

            print("x =", x, "y =", y)

    elif opcion == "4":

        print("\nPrograma terminado.")
        break

    else:

        print("\nOpción no válida.")