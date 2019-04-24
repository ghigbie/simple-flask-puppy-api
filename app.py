from flask import Flask
from falsk_restful import Resource, Api

app = Flask (__name__)
api = Api(app)

puppies = []

class PuppyNames(Resource):

    def get(self):
        pass
    
    def post():
        pass
    
    def delete():
        pass
        
if __name__ == '__main__':
    app.run(Debug=True)