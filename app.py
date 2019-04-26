from flask import Flask
from flask_restful import Resource, Api

app = Flask (__name__)
api = Api(app)

puppies = []

class PuppyNames(Resource):

    def get(self, name):
        for pup in puppies:
            if pup.name == name:
                return pup
        return {'name' : "None"}
    
    def post(self, name):
        pup = {'name' : name}
        puppies.append(pup)
        return pup
    
    def delete(self, name):
        pass

if __name__ == '__main__':
    app.run(Debug=True)