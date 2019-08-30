# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class OCRMobileAPI(Resource):
    def get(self):
        return {'orders': [{'order_no': 1, 'cust_no': '001'}, {'order_no': 1, 'cust_no': '001'}, {'order_no': 1, 'cust_no': '001'}]}


api.add_resource(OCRMobileAPI, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
