# create a case to add a book , get and the delete

import requests
from tests.payload import *

req = requests.post('http://216.10.245.166/Library/Addbook.php', json=get_payload(), headers={'Content-Type' : 'application/json;charset=UTF-8'})

request_response = req.json()
print((request_response))
get_book_id = request_response['ID']

get_book = requests.get('http://216.10.245.166/Library/GetBook.php' , params={'ID':get_book_id})
get_book_repsonse = get_book.json()

print(get_book_repsonse)

# delete a book
delt = requests.post('http://216.10.245.166/Library/DeleteBook.php' , json = {'ID' : get_book_id} , headers={'Content-Type' : 'application/json;charset=UTF-8'})

del_resp = delt.json()

print(del_resp)