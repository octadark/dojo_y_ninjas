from app_flask.configuracion.mysqlconnection import connectToMySQL
from app_flask import BASE_DATOS

class Ninja:
    def __init__(self, datos):
        self.id = datos['id']
        self.first_name = datos['first_name']
        self.last_name = datos['last_name']
        self.age = datos['age']
        self.created_at = datos['created_at']
        self.updated_at = datos['updated_at']
        self.dojo_id = datos['dojo_id']

    @classmethod
    def agregar_uno(cls, datos):
        query = """
                INSERT INTO ninjas(first_name, last_name, age, dojo_id)
                VALUES (%(nombre)s,%(apellido)s,%(edad)s,%(dojo_id)s);
                """
        return connectToMySQL(BASE_DATOS).query_db(query, datos)