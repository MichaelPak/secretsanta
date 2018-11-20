from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def template_test():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        try:
            pass
        except Exception:
            return render_template('login.html')
