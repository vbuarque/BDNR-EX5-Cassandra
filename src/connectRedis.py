import redis

def connect():
    myRedis = redis.Redis(
    host='<endpoint público>', # Coloque o seu host
    port='<porta>', # Coloque a sua porta
    password='<password>') # Coloque a senha do seu BD
    return connectRedis