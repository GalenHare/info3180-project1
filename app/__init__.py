from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "fm1t0th3w0rld"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://gbnzfrjuewwprw:54d6d079b4896e282ba01d7c1e95d2ffa10caeeff78930cb5e8f026941fd51a5@ec2-75-101-131-79.compute-1.amazonaws.com:5432/df7l80r92j8bjj"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
UPLOAD_FOLDER='./app/static/uploads'

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
