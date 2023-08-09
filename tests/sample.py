import json

json1 = '{"name": "Pavan" ,"lang" : ["java", "python"]}'

# to parser use method called - loads - this converts the json string into dicitionary

dict_json = json.loads(json1)
print(dict_json)

print(dict_json['name'])

list_lang = dict_json['lang']

print(list_lang[0])

print(dict_json['lang'][0])

# how to  take json from a file and extract it and parse
f = open('sample.json')
data = json.load(f)
print(data)
print(data['courses'])

for coursed in data['courses']:
    if coursed['title'] == 'RPA' :
        print(coursed['price'])
