from flask_api import FlaskAPI
from flask_restful import Api
from flask_cors import CORS
import os

api_version = '/v1'

app = FlaskAPI(__name__)
CORS(app)
Rapi = Api(app)


@app.route('/', methods=['GET'])
def index():
    return {'version': 'Pomidor - version 1.2.3'}, 200


app.debug = True
host = os.environ.get('IP', '0.0.0.0')
port = int(os.environ.get('PORT', 5000))
app.run(host=host, port=port)

