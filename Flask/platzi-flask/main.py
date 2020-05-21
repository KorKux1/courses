from flask import request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_login import login_required, current_user

from app import create_app
from app.forms import TodoForm

from app.firestore_service import get_users, get_todos, todo_put

import unittest

app = create_app()

""""
Errores
"""
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def server_error(error):
    return render_template("500.html", error=error)

""""
Rutas
"""
@app.route('/')
def index():
    user_ip = request.remote_addr  # Remote address es la IP del usuario.
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return response


@app.route('/hello', methods=['GET', 'POST'])
@login_required
def hello():
    user_ip = session.get('user_ip')
    username = current_user.id

    todo_form = TodoForm()

    

    context = {
        'user_ip':user_ip,
        'todos': get_todos(user_id=username),
        'username': username,
        'todo_form': todo_form
    }

    if todo_form.validate_on_submit():
        todo_put(user_id=username, description=todo_form.description.data)
        flash('Tu tarea se creo con éxito')
        return redirect(url_for('hello'))

    return render_template('hello.html', **context) #Los ** expanden el diccionario.


""""
COMMANDS
"""
@app.cli.command()
def test():
    """"
    El discover buscará todas las pruebas en la carpeta test para que el TextTestRunner las corra
    El decorador permite poder ejecutar Flash test desde la consola de flask 
    """
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)




