from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()