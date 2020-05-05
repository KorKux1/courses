from flask import Flask

app = Flask(__name__) # __name__ indica que el nombre de la aplicación será el nombre del archivo


@app.route('/')
def hello():
    return "Hello, World Flask"