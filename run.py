from flask import Flask
from app.views.users import app

if __name__ == '__main__':
    app.run( port=5000, debug=True)


    # web: gunicorn run:app