import requests

url = "http://hotels4.p.rapidapi.com/locations/search"

querystring = {"query":"India"}

headers = {
    'x-rapidapi-key': "19d0da3691msh95762193c52612cp1c9687jsnb2c7b69f10e8",
    'x-rapidapi-host': "hotels4.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)