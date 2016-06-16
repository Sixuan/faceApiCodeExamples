import pycurl, json

add_person_url = 'http://120.76.26.101:8081/faceApi/persons'

data = json.dumps({"app_key": "123", "app_secret": "321", "name": "ning", "group_ids": [1]})

c = pycurl.Curl()
c.setopt(c.URL, add_person_url)
c.setopt(c.HTTPHEADER, ['Content-Type: application/json','Accept: application/json'])
c.setopt(c.POST, 1)
c.setopt(c.POSTFIELDS, data)
c.perform()

# {
#         "app_key" : "575ac5223a3f9",
#     "app_secret" : "575ac5223a441",

#     "name" : "trump",
#     "group_ids" : [3]
# }