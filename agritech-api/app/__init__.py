from flask import Flask
from database import DatabaseConnection

app = Flask(__name__)

database_connection = DatabaseConnection()
database_connection.create_tables()

from app.views import users
from app.views import produce
from app.views import client_request