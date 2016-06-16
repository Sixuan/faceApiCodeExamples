import pycurl, json

upload_photo_url = 'http://120.76.26.101:8081/faceApi/persons/faces'

c = pycurl.Curl()
c.setopt(c.URL, upload_photo_url)
c.setopt(c.HTTPHEADER, ['Accept: application/json'])
c.setopt(c.POST, 1)
c.setopt(pycurl.HTTPPOST, [
	("image", (c.FORM_FILE, "/Users/sixuanliu/Desktop/demo/ning.jpg")),
	("app_key", "123"),
	("app_secret", "321"),
	("person_id", "47")
	])
c.perform()
