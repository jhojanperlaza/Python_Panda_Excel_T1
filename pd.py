#!/usr/bin/python3
import MySQLdb


def puntod(name_table, list_elements):

    # conexion a base de datos
    user = 'root'
    password = 'mypass'
    database = 'estudiantes'

    mydb = MySQLdb.connect(host="localhost",
                           port=3306, user=user,
                           password=password,
                           database=database)

    mycursor = mydb.cursor()

    if name_table == 'estudiantes':
        q1 = "INSERT INTO {} (id, nombre, carrera_id, departamento_id, municipio_id) VALUES ({},'{}',{},{},{})".format(
            name_table, list_elements[0], list_elements[1].upper(), list_elements[2], list_elements[3], list_elements[4])

    elif name_table == 'notas':
        q1 = "INSERT INTO {} (curso, estudiante_id,  materia_id, carrera_id, nota) VALUES ('{}',{},{},{},{})".format(
            name_table, list_elements[0], list_elements[1], list_elements[2], list_elements[3], list_elements[4])

    else:
        q1 = "INSERT INTO {} (id, nombre) VALUES ({}, '{}')".format(
            name_table, list_elements[0], list_elements[1].upper())

    mycursor.execute(q1)
    mydb.commit()

    # cierra de la conexion
    mycursor.close()
    mydb.close()
