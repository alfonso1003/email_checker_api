from flask import Flask, request
from flask_restful import Resource, Api

from email_list_checker import EmailListChecker

# curl -H "Content-Type: application/json" -X POST -d '{"email_list": ["test.email@gmail.com", "test.email+spam@gmail.com", "testemail@gmail.com", "alfonso@gmail.com"]}' http://127.0.0.1:5000/

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def post(self):
        request_json = request.json
        email_list = request_json.get('email_list', [])    
        elc = EmailListChecker(email_list)
        if elc.valid_email_list:
            return {"unique_email_count": elc.unique_email_count}, 200
        else:
            return {"error": "invalid email address"}, 400
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)