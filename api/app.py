import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ljjr1989jjlyyaf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.abspath('checklist.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True  # Exibir mensagens detalhadas no SQLAlchemy
app.config['DEBUG'] = True  # Ativar o modo de depuração

db = SQLAlchemy(app)
csrf = CSRFProtect(app)

from api import routes
