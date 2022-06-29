from flask import jsonify
import simplejson as json
from bson import json_util,ObjectId

import connectMongo as connectMongo

def searchSellers():
  bd_MercadoLivre = connectMongo.connect()
  collection = bd_MercadoLivre.seller

  document = collection.find()

  retorno = []
  for x in document:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))

  return json.dumps(retorno)

def searchID(request):
  seller = request.get_json()
  bd_MercadoLivre = connectMongo.connect()
  collection = bd_MercadoLivre.seller

  document = collection.find({"_id": ObjectId(seller["id"])})

  retorno = []
  for x in document:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))

  return json.dumps(retorno)

def insert(request):
  seller = request.get_json()
  bd_MercadoLivre = connectMongo.connect()
  collection = bd_MercadoLivre.seller
  collection.insert_one(seller)
  
  return json.dumps({
    "status": "O vendedor foi inserido com sucesso!",
    "vendedor":json.loads(json_util.dumps(seller))
  })
  
def delete(request):
  seller = request.get_json()
  bd_MercadoLivre = connectMongo.connect()
  collection = bd_MercadoLivre.seller

  try:
    collection.delete_one({"_id": ObjectId(seller["id"])})
    return json.dumps({"status": "O vendedor foi deletado com sucesso!"})
  except:
    return json.dumps({"message": "Vish, não foi dessa vez :("})


def insertSeller():
  bd_MercadoLivre = connectMongo.connect()
  bd_MercadoLivre.seller.insert_many({
    "nome":"Irineu da silva",
    "cnpj":"54.531.163/0001-43",
    "email":"irineusilva@gmail.com",
    "endereco": {
        "rua":"Pau D'Arco Roxo",
        "numero":53,
        "estado":"SP",
        "cidade":"São Paulo"
    },
    "telefone":"12982229518"
  })
  return jsonify(message="success")