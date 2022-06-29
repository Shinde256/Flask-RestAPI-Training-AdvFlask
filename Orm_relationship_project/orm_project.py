from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/temp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column('emp_id',db.Integer(),primary_key=True)
    name = db.Column('emp_name',db.String(30))
    adrref = db.relationship('Address',uselist=True,lazy=False,backref='empref')

class Address(db.Model):
    adrid = db.Column('adr_id',db.Integer(),primary_key=True)
    city = db.Column('emp_city', db.String(30))
    empid = db.Column('emp_id',db.ForeignKey('employee.emp_id'), unique=True, nullable=True)

if __name__ == '__main__':
    db.create_all()