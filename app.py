from flask import Flask
from app import routes
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
db = SQLAlchemy(app)