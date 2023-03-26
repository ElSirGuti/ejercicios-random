# Faltó el profesor a clase y los alumnos van a armar su propia clase
# El alumno mas viejo será el profesor y el más joven su asistente

# Función para obtener al asistente y el profesor basado en la edad
def obtener_alumnos(cantidad):

    # Lista de alumnos
    alumnos = []

    # Bucle for que pide la información de cada alumno
    for i in range(cantidad):
        nombre = input("Ingrese el nombre del alumno número " + str(i+1) +" : ")
        edad = int(input("Ingrese la edad del alumno número " + str(i+1) +" : "))
        alumno = (nombre,edad)

        # Agrega la información a la lista
        alumnos.append(alumno)

    # Se ordenan de mayor a menor basado en la edad
    alumnos.sort(key=lambda x:x[1])

    # alumnos[x] retorna una tupla con (nombre,edad) y después accedemos al
    # nombre para definir al asistente y profesor
    asistente = alumnos[0][0]
    profesor = alumnos[-1][0]
    return asistente,profesor

# Función principal del programa
def main():
    # Se solicita la cantidad de alumnos
    cant = int(input("Ingrese la cantidad de alumnos que asistieron: "))

    # Se desempaqueta lo que retorna la función
    asistente,profesor = obtener_alumnos(cant)

    # Salida formateada
    print(f"El profesor es: {profesor} y su asistente es: {asistente}")

main()





