import requests
import json

class exampleREST():
	
	def __init__(self, url):
		self.url = url 
		self.session = requests.Session()

	def makeRequest (self, method, data, header):
		request = requests.Request(method,
				self.url,
				data = data,
				headers = header
		)
		return request.prepare()
	
	def getResponse(self, request):
		return self.session.send(request,
			verify=True	
		)

if __name__ == '__main__':
	google = exampleREST('https://www.google.com/')
	
	#your mom is a json object
	robertsMom = dict()

	#She's also good
	robertsMom = {'State' : 'Good'}

	#Your mom can have an array
	robertsMom['likes'] = [0, 1 , 2 , 3]
	
	#I'm googling your mom, Make your own header
	robertsRealMom = google.makeRequest('POST',
		json.dumps(robertsMom),
		robertsMom
	)
	
	responseFromGoogle = google.getResponse(robertsRealMom)
	
	print(responseFromGoogle.status_code) 
