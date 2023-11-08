from app_flask.configuracion.mysqlconnection import connectToMySQL
from app_flask.modelos import modelo_ninjas
from app_flask import BASE_DATOS

class Dojo:
    def __init__(self, datos):
        self.id = datos['id']
        self.nombre = datos['nombre']
        self.created_at = datos['created_at']
        self.update_at = datos['update_at']
        self.ninjas = []
    
    @classmethod
    def agregar_uno(cls, datos):
        query = """
                INSERT INTO dojo (nombre)
                VALUES (%(nombre)s);
                """
        return connectToMySQL(BASE_DATOS).query_db(query, datos)

    @classmethod
    def seleccionar_todos(cls):
        query = """
                SELECT *
                FROM dojo;
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query)
        lista_dojos = []
        for renglon in resultado:
            lista_dojos.append(cls(renglon))
        return lista_dojos

    @classmethod
    def seleccionar_uno_con_ninjas(cls, datos):
        query = """
                SELECT *
                FROM dojo LEFT JOIN ninjas
                    ON dojo.id = ninjas.dojo_id
                WHERE dojo.id = %(dojo_id)s;
                """
        resultado = connectToMySQL(BASE_DATOS).query_db(query, datos)
        dojo = Dojo(resultado[0])
        print (resultado)
        for renglon in resultado:
            if renglon['age'] != None:
                ninja = {
                    'id' : renglon['ninjas.id'],
                    'first_name' : renglon['first_name'],
                    'last_name' : renglon['last_name'],
                    'age' : renglon['age'],
                    'created_at' : renglon['ninjas.created_at'],
                    'updated_at' : renglon['updated_at'],
                    'dojo_id' : renglon['id']
                    
                }
                dojo.ninjas.append(modelo_ninjas.Ninja(ninja))
        return dojo
    