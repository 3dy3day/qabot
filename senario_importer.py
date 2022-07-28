from elasticsearch import Elasticsearch
from csv import DictReader

csv_file = "data.csv"
elasticsearch_host = "localhost"
index_name = "past_cases"

es = Elasticsearch([f"http://{elasticsearch_host}:9200"])

with open(csv_file, "rt", encoding = "utf-8") as file:
    reader = DictReader(file)
    for row in reader:
        doc = row
        key_id = doc["_key_ID"]
        print(key_id)
        es.index(index = index_name, id = key_id, body = doc)