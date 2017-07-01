# -*- coding:utf-8 -*-
# @author:Eric Luo
# @file:flaskadmin1.py
# @time:2017/3/28 0028 15:43
from flask import Flask
from flask_admin import Admin

app = Flask(__name__)

admin = Admin(app, name='microblog', template_mode='bootstrap3')
# Add administrative views here

app.run()
