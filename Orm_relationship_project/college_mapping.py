
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/temp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


stud_address = db.Table('stud_address',
db.Column('st_id',db.ForeignKey('student.stud_id'),unique=False),
db.Column('adr_id',db.ForeignKey('address.adr_id'),unique=False))


class Student(db.Model):
    id = db.Column('stud_id',db.Integer(),primary_key=True)
    name=db.Column('stud_name',db.String(30))
    adrefs = db.relationship ('Address',secondary=stud_address,backref=db.backref('studref',lazy=True))

class Address(db.Model):
    id = db.Column('adr_id',db.Integer(),primary_key=True)
    city=db.Column('city',db.String(30))
if __name__=='__main__':
    db.create_all()