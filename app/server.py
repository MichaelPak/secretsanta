import logging

from flask import Flask, render_template, request

from app import storage

logger = logging.getLogger(__name__)
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def template_test():
    if request.method == 'GET':
        return render_template('login.html')
    else:

        login = request.form.get('login').lower()
        password = request.form.get('password')
        if storage.check_password(login, password):
            user = storage.get_user(login)
            return render_template('name.html', user=user, users=storage.in_game_list(), login=login)
        else:
            return render_template('login.html')
