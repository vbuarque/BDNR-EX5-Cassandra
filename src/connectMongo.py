from pymongo import MongoClient

def connect():
  client = MongoClient("mongodb+srv://<username>:<password>@vinicius.t09er.mongodb.net/?retryWrites=true&w=majority")
  db_MercadoLivre = client['mercadolivre']

  return db_MercadoLivre