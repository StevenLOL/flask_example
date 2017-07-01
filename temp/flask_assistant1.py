# -*- coding:utf-8 -*-
# @author:Eric Luo
# @file:flask_assistant1.py
# @time:2017/6/27 0027 15:20
from flask import Flask
from flask_assistant import Assistant, tell

app = Flask(__name__)
assist = Assistant(app)

@assist.action('Demo')
def hello_world():
    speech = 'Microphone check 1, 2 what is this?'
    return tell(speech)

if __name__ == '__main__':
    app.run(debug=True)