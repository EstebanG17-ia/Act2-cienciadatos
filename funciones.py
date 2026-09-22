"""
Actividad Práctica: Evaluación de la Ecuación de la Recta
Asignatura: Ciencia de Datos
Alumno: Gomez Estrada Esteban
Matrícula: 2403230186
Fecha: 21/Septiembre/2026
"""

def obtener_parametros(funcion):
    """
    Obtiene la pendiente m y la ordenada al origen b
    de una función escrita como cadena.
    """

    funcion = funcion.replace(" ", "")
    funcion = funcion.lower()

    if "x" not in funcion:
        raise ValueError("La función debe contener la variable x.")

    partes = funcion.split("x")

    parte_m = partes[0]
    parte_b = partes[1]

    if parte_m == "" or parte_m == "+":
        m = 1
    elif parte_m == "-":
        m = -1
    else:
        m = float(parte_m)

    if parte_b == "":
        b = 0
    elif parte_b.startswith("+"):
        b = float(parte_b[1:])
    else:
        b = float(parte_b)

    return m, b