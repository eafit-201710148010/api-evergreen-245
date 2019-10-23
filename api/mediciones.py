from flask import jsonify, request
from api.db import cnx

class Medicion:
    global cur 
    cur = cnx.cursor()

    def list():
        lista = []
        cur.execute("SELECT * FROM mediciones")
        rows = cur.fetchall()
        columns = [i[0]for i in cur.description]
        #for row in rows:
         #   registro = zip(columns, row)
          #  json = dict(registro)
           # lista.append(json)
        #return jsonify(lista)
        #cnx.close
        for i in range(len(columns)):
            columns[i] = str(columns[i])

        for row in rows:

            nuevaRow = list(row)
            
            for i in range(len(nuevaRow) - 1):
                nuevaRow[i] = str(nuevaRow[i])

            registro = zip(columns, nuevaRow)

            diccionario = dict(registro)

            lista.append(diccionario)

        return lista

        cnx.close()
    
    def create(body):
        data = (body['fecha'],body['origen'],body['valor'],body['codigoSensor'],body['observacion'])

        sql = "INSERT INTO mediciones(fecha, origen, valor, codigoSensor, observacion) VALUES(%s, %s, %s, %s, %s)"
        cur.execute(sql,data)
        cnx.commit()
        return {'estado': "Insertado"}, 200
        cnx.close()
