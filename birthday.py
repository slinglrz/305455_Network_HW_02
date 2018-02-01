from flask import Flask , request
from flask_restful import Resource , Api,reqparse
from datetime import datetime
import json ,time

app = Flask (__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('birth')

def age(date):
	today = date.today()
	return today.year-born.year-((today.month, today.day) < (born.month, born.day))
	
class Hello(Resource):
	def get(self):
		args = parser.parse_args()
	 	birthdate = args['birth']
		birthtime = datetime.strptime(birthdate, '%d-%m-%Y')				
		age = int(calculate_age(birthtime))
		return {"birth":birthtime,"age":age}

api.add_resource(Hello,'/birthdate')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5555)

