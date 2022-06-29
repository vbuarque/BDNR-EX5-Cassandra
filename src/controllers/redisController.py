from datetime import date
import simplejson as json
from bson import json_util, ObjectId

import connectRedis as connectRedis
import connectMongo as connectMongo
import src.utils.dias_do_mes as dias_do_mes

cursor = connectRedis.connect()
bd_MercadoLivre = connectMongo.connect()

day = date.day()

daySTRING = day.strftime("%d/%m/%Y")


def incrementProductViews(request):
    collection = bd_MercadoLivre.product

    product = request.get_json()
    try:
        document = collection.find({"_id": ObjectId(product["id"])})
        for x in document:
            retorno = json.loads(json_util.dumps(x))

        cursor.incr(f'produto:{product["id"]}:{daySTRING}:views_dia')
        cursor.incr(f'produto:{product["id"]}:views_total')
        return json.dumps({
            "produto": retorno,
            "visualizacoesHOJE": {
                "data_hoje": daySTRING,
                "visualizacoesDIA": int(cursor.get(f'produto:{product["id"]}:{daySTRING}:visualizacoesDIA')),
            },
            "vizualizacoesTOTAL": int(cursor.get(f'produto:{product["id"]}:vizualizacoesTOTAL'))
        })

    except:
        return json.dumps({
            "message": "Vish, não foi dessa vez :("
        })


def incrementViews():
    cursor.incr(f'pagina:{daySTRING}:visualizacoesDIA')
    cursor.incr(f'pagina:visualizacoesTOTAL')
    return json.dumps({
        "visualizacoesTOTAL": int(cursor.get(f'pagina:visualizacoesTOTAL')),
        "visualizacoesHOJE": {
            "data_hoje": daySTRING,
            "vizualizacoesQNT": int(cursor.get(f'pagina:{daySTRING}:visualizacoesDIA'))
        }
    })


def generalReport():
    listingViewsDay = []
    counterViewsMonthly = 0
    for day in dias_do_mes.dias_do_mes():
        if (cursor.get(f'pagina:{day}:visualizacoesDIA')):
            listingViewsDay.append({
                "dia": day,
                "visualizacoesDIA": int(cursor.get(f'pagina:{day}:visualizacoesDIA'))
            })
            counterViewsMonthly += int(
                cursor.get(f'pagina:{day}:visualizacoesDIA'))
        else:
            listingViewsDay.append({
                "dia": day,
                "visualizacoesDIA": 0
            })

    return json.dumps({
        "visualizacoesTOTAL": int(cursor.get(f'pagina:visualizacoesTOTAL')),
        "visualizacoesMENSAL": counterViewsMonthly,
        "listagemVisualizacoesDia": listingViewsDay
    })


def saveReport():
    try:
        today = date.today()
        daySTRING = today.strftime("%d/%m/%Y")

        report = bd_MercadoLivre.report

        reportSaved = {
            "backup_dia": daySTRING,
            "dados": json.loads(generalReport())
        }

        print(reportSaved)

        report.insert_one(reportSaved)

        return json.dumps({"message": "Seu relatório foi salvo com sucesso!"})

    except:
        return json.dumps({"message": "Vish, não foi dessa vez :("})


def deleteAllKeys():
    cursor.flushall()

    return json.dumps({
        "message": "Todas as chaves foram deletadas com sucesso!"
    })