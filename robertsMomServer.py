from flask import Flask 


app = Flask(__name__)


@app.route("/")
def hello():
	print "this ran"
	return "Works"




@app.route("/robertsMom")
def robertsMom():
	if request.method == 'GET':
		return "You RAN GET"
	elif request.method == 'POST':
		return json.dumps(request.get_json()) 
	else: 
		return "Nope!!"


if __name__ == "__main__":
	app.run(host= '0.0.0.0')
