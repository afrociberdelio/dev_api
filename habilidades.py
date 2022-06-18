import json
from flask_restful import Resource
from flask import request

lista_habilidades = ["Ajax","Lua","Java","Python","C#","Javascript","Django","Flask"]

class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        lista_habilidades.append(dados['habilidade'])
        return lista_habilidades

    def put(self):
        dados = json.loads(request.data)
        lista_habilidades[dados['id']] = dados['habilidade']
        return lista_habilidades

    def delete(self):
        dados = json.loads(request.data)
        lista_habilidades.remove(dados['habilidade'])
        return lista_habilidades