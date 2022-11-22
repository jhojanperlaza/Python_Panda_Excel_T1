#!/usr/bin/python3
import pandas as pd
import MySQLdb

def puntoc(name_archivo):

    # conexion a base de datos
    user = 'root'
    password = 'mypass'
    database = 'estudiantes'

    mydb = MySQLdb.connect(host="localhost",
                           port=3306, user=user,
                           password=password,
                           database=database)
    mycursor = mydb.cursor()
    q1 = "SELECT * FROM municipios"
    mycursor.execute(q1)
    municipios = mycursor.fetchall()
    q2 = "SELECT * FROM departamentos"
    mycursor.execute(q2)
    departamentos = mycursor.fetchall()
    q3 = "SELECT * FROM carreras"
    mycursor.execute(q3)
    carreras = mycursor.fetchall()
    q4 = "SELECT * FROM materias"
    mycursor.execute(q4)
    materias = mycursor.fetchall()
    q5 = "SELECT * FROM notas"
    mycursor.execute(q5)
    notas = mycursor.fetchall()
    q6 = "SELECT * FROM estudiantes"
    mycursor.execute(q6)
    estudiantes = mycursor.fetchall()

    list_elements = []
    id_elements = []

    for id, municipio in municipios:
        list_elements.append(municipio)
        id_elements.append(id)
    df1 = pd.DataFrame(list(zip(id_elements, list_elements)),
                       columns=['id', 'municipios'])

    list_elements.clear(), id_elements.clear()
    for id, departamento in departamentos:
        list_elements.append(departamento)
        id_elements.append(id)
    df2 = pd.DataFrame(list(zip(id_elements, list_elements)),
                       columns=['id', 'departamentos'])

    list_elements.clear(), id_elements.clear()
    for id, carrera in carreras:
        list_elements.append(carrera)
        id_elements.append(id)
    df3 = pd.DataFrame(list(zip(id_elements, list_elements)),
                       columns=['id', 'carreras'])

    list_elements.clear(), id_elements.clear()
    for id, materia in materias:
        list_elements.append(materia)
        id_elements.append(id)
    df4 = pd.DataFrame(list(zip(id_elements, list_elements)),
                       columns=['id', 'materias'])

    list_elements.clear(), id_elements.clear()
    for id, name, carrera, departamento, municipio in estudiantes:
        list_elements.append(name)
        id_elements.append(id)
    df5 = pd.DataFrame(list(zip(id_elements, list_elements)),
                       columns=['id', 'estudiantes'])

    list_estudiantes = []
    list_cursos = []
    list_materias = []
    list_notas = []
    list_carreras = []

    for curso, estudiante, materia, carrera, nota in notas:
        q7 = "SELECT estudiantes.nombre FROM estudiantes INNER JOIN notas ON estudiantes.id=notas.estudiante_id WHERE id={}".format(estudiante)
        mycursor.execute(q7)
        estudiantes_notas = mycursor.fetchall()
        list_estudiantes.append(estudiantes_notas[0][0])
        q8 = "SELECT materias.nombre FROM materias INNER JOIN notas ON materias.id=notas.materia_id WHERE id={}".format(materia)
        mycursor.execute(q8)
        materias_notas = mycursor.fetchall()
        list_materias.append(materias_notas[0][0])
        q9 = "SELECT carreras.nombre FROM carreras INNER JOIN notas ON carreras.id=notas.carrera_id WHERE id={}".format(carrera)
        mycursor.execute(q9)
        carreras_notas = mycursor.fetchall()
        list_carreras.append(carreras_notas[0][0])
        list_notas.append(nota)
        list_cursos.append(curso)

        df6 = pd.DataFrame(list(zip(list_cursos, list_estudiantes, list_materias, list_carreras, list_notas)),
                       columns=['curso', 'estudiantes', 'materias', 'carreras', 'notas'])


    # Escribir los datos en el Excel
    with pd.ExcelWriter(name_archivo) as writer:
        df1.to_excel(writer, sheet_name='Municipios', index=False)
        df2.to_excel(writer, sheet_name='Departamentos', index=False)
        df3.to_excel(writer, sheet_name='Carreras', index=False)
        df4.to_excel(writer, sheet_name='Materias', index=False)
        df5.to_excel(writer, sheet_name='Estudiantes', index=False)
        df6.to_excel(writer, sheet_name='Notas', index=False)

    # cierra de la conexion
    mycursor.close()
    mydb.close()
