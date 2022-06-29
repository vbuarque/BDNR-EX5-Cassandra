from flask import jsonify
import simplejson as json
from bson import json_util,ObjectId

import connectMongo as connectMongo

def searchUser():
  bd_MercadoLivre = connectMongo.connect()
  collection = bd_MercadoLivre.user

  document = collection.find()

  retorno = []
  for x in document:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))

  return json.dumps(retorno)

def searchID(request):
  user = request.get_json()
  bd_MercadoLivre = connectMongo.connect()
  collection = bd_MercadoLivre.user

  document = collection.find({"_id": ObjectId(user["id"])})

  retorno = []
  for x in document:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))

  return json.dumps(retorno)
  

def insert(request):
  user = request.get_json()
  bd_MercadoLivre = connectMongo.connect()
  collection = bd_MercadoLivre.user
  collection.insert_one(user)
  
  return json.dumps({
    "status": "O usuário foi inserido com sucesso!",
    "usuario":json.loads(json_util.dumps(user))
  })

def delete(request):
  user = request.get_json()
  bd_MercadoLivre = connectMongo.connect()
  collection = bd_MercadoLivre.user
  print(user)

  try:
    collection.delete_one({"_id": ObjectId(user["id"])})
    return json.dumps({"status": "O usuário foi deletado com sucesso!"})
  except:
    return json.dumps({"message": "Vish, não foi dessa vez :("})

def insertUser():
  bd_MercadoLivre = connectMongo.connect()
  bd_MercadoLivre.user.insert_many([{
    "nome":"Vinicius Buarque",
    "cpf":"334.221.553-23",
    "endereco": {
        "rua":"Rua dos radialistas",
        "numero":24,
        "estado":"SP",
        "cidade":"São José dos Campos"
    },
    "carrinho":[{
      "produto":{
          "nome": "Mouse gamer",
          "descricao":"Mouse gamer RGB 16000 dpi",
          "preco":150.00,
          "a-vista":100.00,
          "prazo":130.00,
          "uuid-vendedor":"62a129f060f02e9c44d307e8",
      },
      "produto2":{
        "nome": "Headset gamer",
        "descricao":"Headset gamer RGB 7.1",
        "preco":250.00,
        "a-vista":200.00,
        "prazo":230.00,
        "uuid-vendedor":"62a129f060f02e9c44d307e8",
      }}],
      "email":"viniciusbuarque@gmail.com",
      "telefone":"12982229518"
    }])
  return jsonify(message="success")