from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort
import json

app = Flask(__name__)
api = Api(app)


# @app.route('/api/object_detection')
# def image():
#   if request.method == "POST":
#     data = request.form
#     return request.form

class Image(Resource):
  def post(self):
    image_id = json.loads(request.json)['id']
    #result = json.dumps('{"id": {}, "object": [{"label": "book"}]}'.format(image_id))
    #image = Image.open(ByteIO(i))
    #image = np.array(image)
          #request.get_json()
    return image_id


api.add_resource(Image, "/api/object_detection")

if __name__ == "__main__":
  app.run(debug=True)