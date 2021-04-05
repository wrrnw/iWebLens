from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)


class Image(Resource):
  def post(self):
    data = request.get_json()
    return data


api.add_resource(Image, "/api/object_detection")

if __name__ == "__main__":
  app.run(debug=True)