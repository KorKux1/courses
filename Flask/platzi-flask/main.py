from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)  # __name__ indica que el nombre de la aplicación será el nombre del archivo

todos = ['TODO 1', 'TODO 2', 'TODO 3']
@app.route('/')
def index():
    user_ip = request.remote_addr  # Remote address es la IP del usuario.
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    return response


@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip':user_ip,
        'todos':todos
    }
    return render_template('hello.html', **context) #Los ** expanden el diccionario.