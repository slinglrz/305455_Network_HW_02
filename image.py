from flask import Flask , request
from flask_restful import Resource ,Api,reqparse
import json
from werkzeug.datastructures import FileStorage

app = Flask (__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('picture', type=FileStorage, location='files')

class images(Resource):
	def post(self):
		args = parser.parse_args()
		image = args['picture']
		image_name = image.filename
		image.save(image_name)
		return {"code":200,"desc":"Upload success"}
		


api.add_resource(images,'/picture')
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5551)
