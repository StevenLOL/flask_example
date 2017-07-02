from app.main import main
from flask import render_template


@main.route('/machine-learning')
def chat_chatterbot():
    return render_template('machine_learning.html')
