class Libros:
    def __init__(self, título, autor, year):
        self.titulo = título
        self.autor = autor
        self.year = year

    def mostrar_info(self):
        print(f"Título: {self.titulo}. su autor es: {self.autor} y el año de lanzamiento fue: {self.year}")

libros = []

def agregar_libros():
    try:
        libro_nombre = input("Ingresa el nombre del libro: ")
        autor_nombre = input("Ingresa el nombre del autor: ")
        year_lanzamiento = int(input("Ingresa el año de lanzamiento: "))
        datos_libro = Libros(libro_nombre, autor_nombre, year_lanzamiento)
        libros.append(datos_libro)
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

def eliminar_libro():
    libro_buscado = input("Ingresa el título del libro para eliminar: ")
    encontrado = False
    for datos_libro in libros:
        if datos_libro.titulo.lower() == libro_buscado.lower():
            libros.remove(datos_libro)
            print("Libro eliminado exitosamente.\n")
            encontrado = True
            break
    if not encontrado:
        print("Libro no encontrado.\n")

while True:
    print("MENÚ: ")
    print("1. Agregar libro")
    print("2. Mostrar lista de libros")
    print("3. Eliminar libro por título")
    print("4. Salir")

    try:
        option = input("Introduce una opción (1-4): ")
        match option:
            case "1":
                agregar_libros()
            case "2":
                mostrar_libros()
            case "3":
                eliminar_libro()
            case "4":
                print("Programa finalizado. Saliendo...")
                break
            case _:
                print("¡Opción no válida!")
    except ValueError:
        print("ERROR, debes ingresar un número entero.")



