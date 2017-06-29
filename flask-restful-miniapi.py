# -*- coding:utf-8 -*-
# @author:Eric Luo
# @file:excel1.py
# @time:2017/3/13 0013 9:59
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)