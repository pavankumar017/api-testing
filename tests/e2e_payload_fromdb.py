# e2e_payload_fromdb.py  - here we are getting data from DB and then creating a dictionary dynamically 

import requests
from payload import *

payload = build_payload_fromDB()
print(payload)

req = requests.post('http://216.10.245.166/Library/Addbook.php', json=payload, headers={'Content-Type' : 'application/json;charset=UTF-8'})

request_response = req.json()
print((request_response))
get_book_id = request_response['ID']

