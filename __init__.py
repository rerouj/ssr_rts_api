from Client import Client
from pprint import pprint
from pymongo import MongoClient


def main():
    mongo_client = MongoClient('mongodb://localhost:27017/')
    db = mongo_client['test_apirts']
    collection = db["show_test"]

    obj = {"username": "EuVeni0O6q0nKiJXGdFFq0T3GtLEmvrA",
           "password": "MpL1sm6DLLDtxsvh"}
    querystring = {
        "query": "'id'='103'",
        "rows": "1",
        "start": "0",
        "minPublicationDate": "1960",
        "maxPublicationDate": "2020",
        "sort": "publicationDate"
    }

    cl = Client(obj)
    print(cl.token)
    res = cl.request(querystring)
    data = res.json()
    d = data['data']
    filtered = cl.filter_data(data, ['program', 'id'], 103)
    # res = cl.save_data(data, collection)


if __name__ == "__main__":
    main()
