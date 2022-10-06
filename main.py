from tokenize import Name
from webbrowser import get
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names= {"tim":{"age":18, "gender": "male"},
        "bill":{"age":34, "gender": "male"},
        "amy":{"age":24, "gender": "female"}}

class Helloworld(Resource):
    def get(self, name):
        return names[name]

      


api.add_resource(Helloworld, "/hello/<string:name>")


if __name__ == "__main__":
    app.run(debug=True)
