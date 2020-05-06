from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import  StringField, PasswordField, SubmitField
from wtforms.validators import  DataRequired

app = Flask(__name__)  # __name__ indica que el nombre de la aplicación será el nombre del archivo
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'SUPER SECRETO'

todos = ['Comprar Café', 'Enviar solicitud de compra', 'Entregar video al productor']

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Entrar')

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
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    context = {
        'user_ip':user_ip,
        'todos':todos,
        'login_form': login_form
    }
    return render_template('hello.html', **context) #Los ** expanden el diccionario.