#!/usr/bin/python3
import MySQLdb
import pandas as pd


def puntoe():

    # conexion a base de datos
    user = 'root'
    password = 'mypass'
    database = 'estudiantes'

    mydb = MySQLdb.connect(host="localhost",
                           port=3306, user=user,
                           password=password,
                           database=database)
    mycursor = mydb.cursor()
    q1 = "SELECT * FROM notas"
    mycursor.execute(q1)
    notas = mycursor.fetchall()

    list_estudiantes = []
    list_cursos = []
    list_materias = []
    list_notas = []
    list_carreras = []

    for curso, estudiante, materia, carrera, nota in notas:
        q7 = "SELECT estudiantes.nombre FROM estudiantes INNER JOIN notas ON estudiantes.id=notas.estudiante_id WHERE id={}".format(
            estudiante)
        mycursor.execute(q7)
        estudiantes_notas = mycursor.fetchall()
        if len(estudiantes_notas) == 0:
            continue
        list_estudiantes.append(estudiantes_notas[0][0])
        q8 = "SELECT materias.nombre FROM materias INNER JOIN notas ON materias.id=notas.materia_id WHERE id={}".format(
            materia)
        mycursor.execute(q8)
        materias_notas = mycursor.fetchall()
        if len(materias_notas) == 0:
            continue
        list_materias.append(materias_notas[0][0])
        q9 = "SELECT carreras.nombre FROM carreras INNER JOIN notas ON carreras.id=notas.carrera_id WHERE id={}".format(
            carrera)
        mycursor.execute(q9)
        carreras_notas = mycursor.fetchall()
        if len(carreras_notas) == 0:
            continue
        list_carreras.append(carreras_notas[0][0])
        list_notas.append(nota)
        list_cursos.append(curso)

    list_notas.sort(reverse=True)
    print('\n_________________________________________________')
    print('\n5 mejores estudiantes general:')
    print('_________________________________________________\n')
    df1 = pd.DataFrame(list(zip(list_estudiantes[:5], list_notas[:5])),
                       columns=['estudiantes', 'notas'])
    print(df1)
    print('\n_________________________________________________')
    print('\n5 mejores estudiantes por carrera:')
    print('_________________________________________________\n')

    top_carreras = {}
    top_notas = []
    top_names = []
    for new_list in zip(list_estudiantes, list_carreras, list_notas):
        if new_list[1] in top_carreras:
            temp_estudent = top_carreras[new_list[1]]
            if temp_estudent[1] < new_list[2]:
                top_carreras[new_list[1]] = [new_list[0], new_list[2]]
        else:
            top_carreras[new_list[1]] = [new_list[0], new_list[2]]

    for values in top_carreras.values():
        top_names.append(values[0])
        top_notas.append(values[1])

    df2 = pd.DataFrame(list(zip(top_carreras.keys(), top_names, top_notas)),
                       columns=['carrera', 'estudiantes', 'notas'])
    print(df2)

    print('\n_________________________________________________')
    print('\nPromedio general')
    print('_________________________________________________\n')
    promedio = sum(list_notas)/len(list_notas)
    promedio = round(promedio, 3)
    print(promedio)

    print('\n_________________________________________________')
    print('\nPromedio por carrera')
    print('_________________________________________________\n')
    prom_carreras = {}
    for new_list2 in zip(list_carreras, list_notas):
        if new_list2[0] in prom_carreras:
            prom_carreras[new_list2[0]].append(new_list2[1])
        else:
            prom_carreras[new_list2[0]] = [new_list2[1]]

    for key, value in prom_carreras.items():
        prom_carreras[key] = sum(value)/len(value)

    for key, value in prom_carreras.items():
        prom_carreras[key] = round(value, 3)

    df3 = pd.DataFrame(list(zip(prom_carreras.keys(), prom_carreras.values())),
                       columns=['carrera', 'promedio'])
    print(df3)

    # Escribir los datos en el Excel
    with pd.ExcelWriter('puntoe.xlsx') as writer:
        df1.to_excel(writer, sheet_name='PROM1', index=False)
        df2.to_excel(writer, sheet_name='PROM2', index=False)
        df3.to_excel(writer, sheet_name='PROM3', index=False)

    # cierra de la conexion
    mycursor.close()
    mydb.close()
