#!/usr/bin/python3
import pandas as pd
import MySQLdb

def puntob(name_archivo):

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
    q2 = "SELECT * FROM departamentos"
    mycursor.execute(q1)
    municipios = mycursor.fetchall()
    mycursor.execute(q2)
    departamentos = mycursor.fetchall()
    departamentos_list_db = []
    municipios_list_db = []

    for id, municipio in municipios:
        municipios_list_db.append(municipio)
    
    for id, departamento in departamentos:
        departamentos_list_db.append(departamento)


    # lectura del excel
    #archivo = input('Ingerese la ruta del archivo: ')
    archivo = name_archivo

    df_departamentos = pd.read_excel(archivo, sheet_name='departamentos')
    df_municipios = pd.read_excel(archivo, sheet_name='municipios')


    departamentos_list = df_departamentos.values
    municipios_list = df_municipios.values

    #Comparacion de los datos del excel y los datos de la db
    for municipio in municipios_list:
        municipio = municipio[0].upper()
        if municipio not in municipios_list_db:
                q3 = "INSERT INTO municipios (nombre) VALUES (%s);"
                mycursor.execute(q3, (municipio,))
                mydb.commit()


    for departamento in departamentos_list:
        departamento = departamento[0].upper()
        if departamento not in departamentos_list_db:
                q3 = "INSERT INTO departamentos (nombre) VALUES (%s);"
                mycursor.execute(q3, (departamento,))
                mydb.commit()

    #cierra de la conexion
    mycursor.close()
    mydb.close()
