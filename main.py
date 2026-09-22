"""
Actividad Práctica: Evaluación de la Ecuación de la Recta
Asignatura: Ciencia de Datos
Alumno: Gomez Estrada Esteban
Matrícula: 2403230186
Fecha: 21/Septiembre/2026
"""

from funciones import obtener_parametros


funcion = input("Escribe una función lineal: ")

m, b = obtener_parametros(funcion)

print("\nParámetros encontrados:")
print("Pendiente (m):", m)
print("Ordenada al origen (b):", b)