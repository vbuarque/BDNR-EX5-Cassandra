import src.controle.userController as userController
import src.controle.sellerController as sellerController
import src.controle.productController as productController
import src.controle.purchaseController as purchaseController
import src.controle.redisController as redisController



from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def test():
  jsonTest = {"status": "API Online"}
  return jsonify(jsonTest)

#--------------------------------------------------------
#Usuarios
@app.route("/user/insertUser", methods=['POST'])
@cross_origin()
def insertUser():
    return userController.insertUser()

@app.route("/users", methods=['GET'])
@cross_origin()
def users():
	return userController.searchUser()

@app.route("/users", methods=['GET'])
@cross_origin()
def user():
	return userController.searchID(request)

@app.route("/user/create", methods=['POST'])
@cross_origin()
def createUser():
	return userController.insert(request)

@app.route("/user/delete", methods=['DELETE'])
@cross_origin()
def deleteUser():
	return userController.delete(request)

#--------------------------------------------------------
#vendedores
@app.route("/seller/insertSeller", methods=['POST'])
@cross_origin()
def insertSeller():
    return sellerController.insertSeller()

@app.route("/sellers", methods=['GET'])
@cross_origin()
def sellers():
	return sellerController.searchSeller()

@app.route("/seller", methods=['GET'])
@cross_origin()
def seller():
	return sellerController.searchID(request)

@app.route("/seller/create", methods=['POST'])
@cross_origin()
def createSeller():
	return sellerController.insert(request)

@app.route("/seller/delete", methods=['DELETE'])
@cross_origin()
def deleteSeller():
	return sellerController.delete(request)

#--------------------------------------------------------
#Produtos
@app.route("/product/insertProduct", methods=['POST'])
@cross_origin()
def insertProduct():
    return productController.insertProduct()

@app.route("/products", methods=['GET'])
@cross_origin()
def products():
	return productController.searchProduct()

@app.route("/produto", methods=['GET'])
@cross_origin()
def product():
	return productController.searchID(request)

@app.route("/product/create", methods=['POST'])
@cross_origin()
def createProduct():
	return productController.insert(request)

@app.route("/product/delete", methods=['DELETE'])
@cross_origin()
def deleteProduct():
	return productController.delete(request)

#--------------------------------------------------------
#Compras
@app.route("/purchase/insertPurchase", methods=['POST'])
@cross_origin()
def insertPurchase():
    return purchaseController.insertPurchase()

@app.route("/purchases", methods=['GET'])
@cross_origin()
def purchases():
	return purchaseController.searchPurchase()

@app.route("/purchase", methods=['GET'])
@cross_origin()
def compra():
	return purchaseController.searchID(request)

@app.route("/purchase/create", methods=['POST'])
@cross_origin()
def createPurchase():
	return purchaseController.insert(request)

@app.route("/purchase/delete", methods=['DELETE'])
@cross_origin()
def purchaseDelete():
	return purchaseController.delete(request)


# Redis
@app.route("/product/redis/incrementViews", methods=['GET'])
@cross_origin()
def incrementProductViews():
	return redisController.incrementProductViews(request)

@app.route("/website/redis/incrementViews", methods=['GET'])
@cross_origin()
def incrementPageViews():
	return redisController.incrementPageViews()

@app.route("/website/redis/generalReport", methods=['GET'])
@cross_origin()
def generalReport():
	return redisController.generalReport()

@app.route("/redis/deleteAllKeys", methods=['DELETE'])
@cross_origin()
def deleteAllKeys():
	return redisController.deleteAllKeys()

@app.route("/redis/saveReport", methods=['POST'])
@cross_origin()
def saveReport():
	return redisController.saveReport()

if __name__ == '__main__':
	app.run(debug=True)