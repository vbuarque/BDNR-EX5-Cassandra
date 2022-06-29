from flask import jsonify
import simplejson as json
from bson import json_util,ObjectId

import connectMongo as connectMongo

#pesquisa da compra
def searchPurchase():
  bd_MercadoLivre = connectMongo.connect()
  collection = bd_MercadoLivre.purchase

  document = collection.find()

  retorno = []
  for x in document:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))

  return json.dumps(retorno)

#pesquisa do id da compra
def searchID(request):
  purchase = request.get_json()
  bd_MercadoLivre = connectMongo.connect()
  collection = bd_MercadoLivre.purchase

  document = collection.find({"_id": ObjectId(purchase["id"])})

  retorno = []
  for x in document:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))
  
  return json.dumps(retorno)

#inserindo a compra
def insert(request):
  purchase = request.get_json()
  bd_MercadoLivre = connectMongo.connect()
  collection = bd_MercadoLivre.purchase
  collection.insert_one(purchase)
  
  return json.dumps({
    "status": "Sua compra foi inserida com sucesso!",
    "compra":json.loads(json_util.dumps(purchase))
  })

#deletando a compra
def delete(request):
  purchase = request.get_json()
  bd_MercadoLivre = connectMongo.connect()
  collection = bd_MercadoLivre.purchase

  try:
    collection.delete_one({"_id": ObjectId(purchase["id"])})
    return json.dumps({"status": "Sua compra foi excluida com sucesso!"})
  except:
    return json.dumps({"message": "Vish, não foi dessa vez :("})

#inserindo a compra
def insertPurchase():
  bd_MercadoLivre = connectMongo.connect()
  bd_MercadoLivre.purchase.insert_many({
    "usuario": {
      "nome":"Vinicius Buarque",
      "endereco": {
        "rua":"Rua dos radialistas",
        "numero":24,
        "estado":"SP",
        "cidade":"São José dos Campos"
      },
      "produto":[{
          "nome": "Mouse gamer",
          "descricao":"Mouse gamer RGB 16000 dpi",
          "preco":150.00,
          "a-vista":100.00,
          "prazo":130.00,
          "uuid-vendedor":"62a129f060f02e9c44d307e8",
      }],
      "vendedor": {
        "nome":"Irineu da silva",
        "endereco": {
          "rua":"Pau D'Arco Roxo",
          "numero":53,
          "estado":"SP",
          "cidade":"São Paulo"
          }
        },
        "total":100.00,
        "status":"pago",
        "pagamento":"a vista"
    }
  })
  return jsonify(message="sucess")