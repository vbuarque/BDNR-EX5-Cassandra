from flask import jsonify
import simplejson as json
from bson import json_util,ObjectId

import connectMongo as connectMongo

# Achar o produto
def searchProducts():
  bd_MercadoLivre = connectMongo.connect()
  collection = bd_MercadoLivre.product

  document = collection.find()

  retorno = []
  for x in document:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))

  return json.dumps(retorno)

#achar o id do produto
def searchID(request):
  product = request.get_json()
  bd_MercadoLivre = connectMongo.connect()
  collection = bd_MercadoLivre.product

  document = collection.find({"_id": ObjectId(product["id"])})

  retorno = []
  for x in document:
    print(x)
    retorno.append(json.loads(json_util.dumps(x)))
  
  return json.dumps(retorno)

#inserir o produto
def insert(request):
  product = request.get_json()
  bd_MercadoLivre = connectMongo.connect()
  collection = bd_MercadoLivre.product
  collection.insert_one(product)
  
  return json.dumps({
    "status": "Seu produto foi inserido com sucesso!",
    "produto":json.loads(json_util.dumps(product))
  })

#deletar o produto
def delete(request):
  product = request.get_json()
  bd_MercadoLivre = connectMongo.connect()
  collection = bd_MercadoLivre.product

  try:
    collection.delete_one({"_id": ObjectId(product["id"])})
    return json.dumps({"status": "Seu produto foi excluida com sucesso!"})
  except:
    return json.dumps({"message": "Vish, não foi dessa vez :("})

#inserindo a compra
def insertPurchase():
  bd_MercadoLivre = connectMongo.connect()
  bd_MercadoLivre.product.insert_many({
    "nome": "Mouse gamer",
    "descricao":"Mouse gamer RGB 16000 dpi",
    "preco":150.00,
    "a-vista":100.00,
    "prazo":130.00,
    "uuid-vendedor":"62a129f060f02e9c44d307e8",
    "pagamento":"a-vista",
    "status":"pago"
  },
  {
    "nome": "Headset gamer",
    "descricao":"Headset gamer RGB 7.1",
    "preco":250.00,
    "a-vista":200.00,
    "prazo":230.00,
    "uuid-vendedor":"62a129f060f02e9c44d307e8",
    "pagamento":"a-vista",
    "status":"pago"
  })
  return jsonify(message="sucess")