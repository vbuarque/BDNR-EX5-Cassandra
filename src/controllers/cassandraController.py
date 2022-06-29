from datetime import date
import connectCassandra as connectCassandra
import json
import uuid

cursor = connectCassandra.connect()


def show():
    vini_uuid = str(uuid.uuid4())
    cursor.create(path=vini_uuid, document={
        "first_name": "Vinicius",
        "last_name": "Buarque",
    })

    return json.dumps({"hasError": False, "Message": "Tudo ok."})