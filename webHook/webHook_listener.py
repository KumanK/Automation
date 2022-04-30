import requests
import json

webH_URL = 'http://127.0.0.1:5000/webhook'
data = {'suite':'acceptance'}

r = requests.post(webH_URL,data=json.dumps(data), headers={'Content-Type': 'application/json'})
print r.status_code