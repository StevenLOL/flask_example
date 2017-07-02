from app.main import main
from flask import render_template


@main.route('/wit-ai')
def chat_wit():
    return render_template('wit_ai.html')
