from flask import Flask, request, make_response, redirect

app = Flask(__name__)  # __name__ indica que el nombre de la aplicación será el nombre del archivo

@app.route('/')
def index():
    user_ip = request.remote_addr  # Remote address es la IP del usuario.
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    return response


@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    return "Hello, World Flask, tú IP es: {}".format(user_ip)