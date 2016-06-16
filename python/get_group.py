import pycurl, json

get_group_url = 'http://120.76.26.101:8081/faceApi/groups/1?app_key=123&app_secret=321'

c = pycurl.Curl()
c.setopt(c.URL, get_group_url)
c.setopt(c.HTTPHEADER, ['Content-Type: application/json','Accept: application/json'])
c.setopt(c.POST, 0)
c.perform()
