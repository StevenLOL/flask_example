# -*- coding:utf-8 -*-
# @author:Eric Luo
# @file:excel1.py
# @time:2017/3/13 0013 9:59
from flask import Flask, request
from flask_restful import Resource, Api
from requests import put, get
put('http://localhost:5000/todo1', data={'data': 'Remember the milk'}).json()
get('http://localhost:5000/todo1').json()
put('http://localhost:5000/todo2', data={'data': 'Change my brakepads'}).json()
get('http://localhost:5000/todo2').json()

class Todo1(Resource):
    def get(self):
        # Default to 200 OK
        return {'task': 'Hello world'}

class Todo2(Resource):
    def get(self):
        # Set the response code to 201
        return {'task': 'Hello world'}, 201

class Todo3(Resource):
    def get(self):
        # Set the response code to 201 and return custom headers
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')

if __name__ == '__main__':
    app.run(debug=True)