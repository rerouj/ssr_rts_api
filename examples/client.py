from Client import Client


def main():

    """
    go to : https://developer.srgssr.ch/apis/rts-archives-v3
    create your app,
    get your consumer key and secret
    remember, that package is only for accessing the "RTS Archives v3" (broadcast) API
    todo: add other endpoint
    """

    # pass an object with your credentials for generating a token and
    # instantiate a client access to the API
    # username = consumer key
    # password = consumer secret
    obj = {"username": "your_consumer_key",
           "password": "yout_consumer_secret"}

    cl = Client(obj)

    # get your token trough the Client.token parameter
    print(cl.token)

    # pass an object with the desired request
    # inside to the Client.request() method
    querystring = {
        "query": "'id'='103'",
        "rows": "1",
        "start": "0",
        "minPublicationDate": "1960",
        "maxPublicationDate": "2020",
        "sort": "publicationDate"
    }

    results = cl.request(querystring)
    data = results.json()

    # results can be a little bit "too generous"
    # refine the results with the Client.filter() method

    filtered = cl.filter_data(data, ['program', 'id'], 103)  # program id : 103 = Temps Présent

    # save the result with the Client.save() method
    # pass a data and a mongodb collection in parameters

    res = cl.save_data(data, collection)