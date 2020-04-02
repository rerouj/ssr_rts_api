# ssr_rts_api

Connect with ease to the public rts/ssr public API.  
That package is only for accessing the RTS Archives v3 (broadcast) endpoint

Enjoy exploring RTS (radio télévision suisse romande) channel broadcast open data 📺 !

# Get it
```
$ pip install ssr_rts_api
```

# How it works

connect to the RTS archives public api can be a little bit confusing. ssr_rts_api is aimed to resolve that issue.

Go to : https://developer.srgssr.ch/apis/rts-archives-v3
create your app,
Get your consumer key and secret  
Remember, that package is only for accessing the "RTS Archives v3" (broadcast) API
todo: add other endpoint
    
```python
from ssr_rts_api import Client as Cl
```

pass an object with your credentials for generating a token and
instantiate a client access to the API  
username = consumer key
password = consumer secret

```python
obj = {"username": "your_consumer_key",
       "password": "yout_consumer_secret"}

cl = Cl.Client(obj)
```
get your token trough the Client.token parameter
```python
print(cl.token)
```
pass an object with the desired request inside the Client.request() method
```python
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
```

results can be a little bit "too generous"
refine the results with the Client.filter() method
```python
filtered = cl.filter_data(data, ['program', 'id'], 103)  # program id : 103 = Temps Présent
```
save the result with the Client.save() method
pass a data and a mongodb collection in parameters
```python
res = cl.save_data(data, collection)
```

# Credit

Renato Diaz (rerouj)
renatojour@gmail.com