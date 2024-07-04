def registrar_libro():
    coleccion = []
    print("\nPor favor, ingrese los datos del libro a continuación:\n\n")
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    anio_publicacion = input("Año de publicacion: ")
    sku = input("Sku: ")
    coleccion.append(titulo)
    print(coleccion.sort())

def prestar_libro():
    print("Por favor, ingrese su nombre de usuario y SKU:")
    nombre_usuario = input("Nombre de usuario:")
    sku = input("SKU:")

#def listar_libros():

#def imprimir_reporte(): 
    

def menu_bienvenida():

    print("Bienvenido a la biblioteca. Elige una opción para continuar:")
    eleccion = int(input("""\n1.Registrar Libro \n 2.Prestar Libro \n 3.Listar todos los libros \n 4.Imprimir reporte de prestamos \n 5.Salir de la biblioteca\n\n"""))
    if eleccion == 1:
        print(registrar_libro())
    if eleccion == 2:
        print("b")
    if eleccion == 3:
        print("c")
    if eleccion == 4:
        print("d")
    if eleccion == 5:
        print("Has salido exitosamente")
        
    






#def prestar_libro():

#def listar_libros():



print(menu_bienvenida())