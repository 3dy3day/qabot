from elasticsearch import Elasticsearch
import unicodedata

elasticsearch_host = "localhost"
index_name = "past_cases"

es = Elasticsearch([f"http://{elasticsearch_host}:9200"])

def main(keyword1, keyword2):
    query = {
        'query': {
            "bool": {
                "must": [
                    {
                        "match": {"EVE_TROUBLE10": str(keyword1)}
                    },{
                        "match": {"EVE_TROUBLE38": str(keyword2)}
                    },
                ]
            }
        }, 
        "_source": {
            "includes": ["_key_ID", "EVE_TROUBLE58", "EVE_TROUBLE9", "EVE_TROUBLE10", "EVE_TROUBLE11", "startDatetime", "EVE_TROUBLE38", "EVE_TROUBLE40", "EVE_TROUBLE39", "EVE_TROUBLE25", "EVE_TROUBLE41"]
        }
    }
    
    results = es.search(index=index_name, body=query, size=3)
    response_pack = "類似するシナリオが過去に" + str(len(results["hits"]["hits"])) + "件見つかりました <br>"
    for result in results["hits"]["hits"]:
        score = result["_score"]
        key_ID = result["_source"]["_key_ID"]
        machine_name = result["_source"]["EVE_TROUBLE10"]
        machine_maker = result["_source"]["EVE_TROUBLE11"]
        trouble_date = result["_source"]["startDatetime"]
        trouble_situation = result["_source"]["EVE_TROUBLE38"]
        trouble_reason = result["_source"]["EVE_TROUBLE40"]
        trouble_solution = result["_source"]["EVE_TROUBLE41"]
        operator_name = result["_source"]["EVE_TROUBLE25"]

        response = f"""発生日時: {trouble_date} ID: {key_ID} Score: {score}<br> \
            メーカー: {machine_maker} 機械名: {machine_name} <br> \
            発生状況: {trouble_situation} <br> \
            発生原因: {trouble_reason} <br> \
            処置・対策: {trouble_solution} <br> \
            作業者: {operator_name}"""
        # print(response)
        response = unicodedata.normalize('NFKC', response)
        response_pack = response_pack + response + "<br><br>"

    return response_pack