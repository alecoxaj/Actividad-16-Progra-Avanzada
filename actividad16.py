class Libros:
    def __init__(self, título, autor, year):
        self.título = título
        self.autor = autor
        self.year = year

    def mostrar_info(self):
        print(f"Título {self.título} su autor es: {self.autor} y el año de lanzamiento fue: {self.year}")

libros = []

def agregar_libros():
    try:
        libro_nombre = input("Ingresa el nombre del libro: ")
        autor_nombre = input("Ingresa el nombre del autor: ")
        year_lanzamiento = int(input("Ingresa el año de lanzamiento: "))
        datos_libro = Libros(libro_nombre, autor_nombre, year_lanzamiento)
        libros.append(libro_nombre)
        print("Libro agregado exitosamente")
    except ValueError:
        print("El año de lanzamiento debe ser un entero")

def mostrar_libros():
    if not libros:
        print("No hay libros registrados.\n")
    else:
        print("Libros registrados: ")
        i = 1
        for datos_libro in libros:
            print(f"{i}. ", end="")
            datos_libro.mostrar_info()
            i += 1
        print()



