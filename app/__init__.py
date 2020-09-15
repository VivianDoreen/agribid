from flask import Flask
from database import DatabaseConnection
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

database_connection = DatabaseConnection()
database_connection.create_tables()

from app.views import users
from app.views import produce
from app.views import client_request