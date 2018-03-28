import requests
import json

url = 'http://127.0.0.1:5000/api/person'
headers = {'Content-Type': 'application/json'}
p={'name': 'newuser'}
response = requests.post(url, data=json.dumps(p), headers=headers)
print(response.json())
response = requests.get(url, headers=headers)
assert response.status_code == 200
print(response.json())
