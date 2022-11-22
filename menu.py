from pb import puntob
from pc import puntoc
from pd import puntod
from pe import puntoe
import MySQLdb


# incorporamos el parámetro para mostrar el nombre del menú
def mostrar_menu(nombre, opciones):
    print(f'# {nombre}. Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (opcion_select := input('Input: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return opcion_select


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


# incorporamos el parámetro para mostrar el nombre del menú
def generar_menu(nombre, opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(nombre, opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Opción 1: Crear base datos', funcion1),
        # la acción es una llamada a submenu que genera un nuevo menú
        '2': ('Opción 2: Importar datos de Excel ', submenu1),
        '3': ('Opción 3: Exportar datos a un Excel', submenu2),
        '4': ('Opción 4: Registrar datos en las tablas', submenu3),
        '5': ('Opción 5: Informes de estudiantes curso 2022-2', funcion5),
        '6': ('Salir', salir)
    }
    # indicamos el nombre del menú
    generar_menu('Menú principal', opciones, '6')


def submenu1():
    opciones = {
        'a': ('Ingerese la ruta y nombre del archivo (ej: ./ejemplo.xlsx)', funcion2),
        'b': ('Volver al menú principal', salir)
    }
    generar_menu('Submenú', opciones, 'b')  # indicamos el nombre del submenú


def submenu2():
    opciones = {
        'a': ('Ingerese el nombre del archivo (ej: puntoc.xlsx)', funcion3),
        'b': ('Volver al menú principal', salir)
    }
    generar_menu('Submenú', opciones, 'b')  # indicamos el nombre del submenú


def submenu3():
    opciones = {
        'a': ('Estudiantes', funcion4_Estudiantes),
        'b': ('Materias', funcion4_Materias),
        'c': ('Notas', funcion4_Notas),
        'd': ('Carreras', funcion4_Carreras),
        'e': ('Municipios', funcion4_Municipios),
        'f': ('Departamentos', funcion4_Departamentos),
        'g': ('Volver al menú principal', salir)
    }
    # indicamos el nombre del submenú
    generar_menu('Submenú Tablas', opciones, 'g')


# A partir de aquí creamos las funciones que ejecutan las acciones de los menús

def funcion1():
    # conexion a base de datos
    user = 'root'
    password = 'mypass'
    mydb = MySQLdb.connect(host="localhost",
                           port=3306, user=user,
                           password=password)
    mycursor = mydb.cursor()

    # Leer archivo para crear base de datos
    fd = open('pa.sql', 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')
    for command in sqlCommands:
        try:
            mycursor.execute(command)
        except:
            pass
    print("\n___________________________________\n")
    print('Base de datos creada correctamente')
    print("___________________________________")


def funcion2():
    name_archivo = input()
    puntob(name_archivo)
    print("\n_________________________________________\n")
    print('Lectura de Excel realizada correctamente')
    print("_________________________________________")


def funcion3():
    name_archivo = input()
    puntoc(name_archivo)
    print("\n____________________________________________\n")
    print('Escritura del Excel a la db realizada correctamente')
    print("____________________________________________")


def funcion4_Estudiantes():
    list_return = []
    list_return.append(input('Id: '))
    list_return.append(input('Nombre: '))
    list_return.append(input('Carrera id: '))
    list_return.append(input('Departamento id: '))
    list_return.append(input('Municipio id '))

    puntod('estudiantes', list_return)


def funcion4_Materias():
    list_return = []
    list_return.append(input('Id: '))
    list_return.append(input('Nombre: '))

    puntod('materias', list_return)


def funcion4_Notas():
    list_return = []
    list_return.append(input('Curso: '))
    list_return.append(input('Id del studiante: '))
    list_return.append(input('Id de la materia: '))
    list_return.append(input('Id de la Carrera: '))
    list_return.append(input('Nota: '))

    puntod('notas', list_return)


def funcion4_Carreras():
    list_return = []
    list_return.append(input('Id: '))
    list_return.append(input('Nombre: '))

    puntod('carreras', list_return)


def funcion4_Municipios():
    list_return = []
    list_return.append(input('Id: '))
    list_return.append(input('Nombre: '))

    puntod('municipios', list_return)


def funcion4_Departamentos():
    list_return = []
    list_return.append(input('Id: '))
    list_return.append(input('Nombre: '))

    puntod('departamentos', list_return)


def funcion5():
    puntoe()


def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()  # iniciamos el programa mostrando el menú principal
