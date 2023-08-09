import requests
import  json
from config import *
from resources import *
 
url = get_config()['API']['endpoint'] + Api_resources.getBook


response = requests.get(url , params={'ID':'bcd227'} )

json_res = response.json()
print((json_res))

# retrivening the isbn code
print(json_res[0]['isbn'])

print(response.status_code)
assert response.status_code == 200
