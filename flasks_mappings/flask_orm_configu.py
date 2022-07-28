from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/ormdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False  #dont show any warning messages from sqlalchemy-->
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)


class Employee(db.Model):  #model class -> entity --> mapping ahe --> database sbt
    id = db.Column('emp_id',db.Integer(),primary_key=True)          # int
    name = db.Column('emp_name',db.String(40))                      # varchar(40)
    email = db.Column('emp_email',db.String(40),unique=True)

    address = db.relationship("Address",uselist=False,lazy=True,backref="employee")                                 #no impact on db side--> user fetch karyla easy hoel

#lazy -->
    #emp = Employee.query.filter_by(id=101)         #lazy=True --> Lazy loading --> lazy=False-- eager loading
    #print(emp.__dict__)    # no address                                        # u will get an address here--> eager loading
    #emp.address        --> will fire a query on db --> on demand

class Address(db.Model):
    id = db.Column('adr_id', db.Integer(), primary_key=True)            #primary key(aid)
    city = db.Column('adr_city', db.String(40))  #4444
    state = db.Column('adr_state', db.String(40))
    pincode = db.Column('pincode', db.Integer())

    empid = db.Column('emp_id',db.ForeignKey('employee.emp_id'),unique=True,nullable=True)        # fk key constraint hoel

if __name__ == '__main__':                          #unique=True  : 1-1         ,               nullable=True:looslycoupled

    emp = Employee.query.filter_by(id=2).first()    # not here
    emp.name="Yogesh"
    db.session.commit() # update--
    #emp.__dict__.pop('_sa_instance_state')
    print(emp.__dict__)
    print(emp.address.city)  # ithe milel
    import sys
    sys.exit(0)
   #db.create_all()
    #




    emp  = Address.query.all()      #emp --> only emp       ---> addresss --> empid:----> get employee object
    for e in emp:
        e.__dict__.pop('_sa_instance_state')
        print(e.__dict__)

    import sys
    sys.exit(0)

    city = input('Enter City Name :')

    if city.isalpha():
        ad1 = Address(city=city, state='MH1', pincode=129022)
        db.session.add(ad1)
        db.session.commit()
    else:
        print('Invalid City Name...!')
    import sys
    sys.exit(0)
    ad1 = Address(id=101,city='Pune1',state='MH1',pincode=129022)
    ad2 = Address(id=102, city='Pune2', state='MH2', pincode=229022)
    ad3 = Address(id=103, city='Pune3', state='MH3', pincode=339022)
    ad4 = Address(id=104, city='Pune4', state='MH4', pincode=449022)
    ad5 = Address(id=105, city='Pune5', state='MH5', pincode=559022)

    ad1.empid = 4
    ad2.empid = 2

    db.session.add_all([ad1,ad2,ad3,ad4,ad5])
    db.session.commit()

    import sys
    sys.exit(0)
    e1 = Employee(id=1,name='XXXX1',email='abc1@gmail.com')
    e2 = Employee(id=2, name='XXXX2', email='abc2@gmail.com')
    e3 = Employee(id=3, name='XXXX3', email='abc3@gmail.com')
    e4 = Employee(id=4, name='XXXX4', email='abc4@gmail.com')
    db.session.add_all([e1,e2,e3,e4])   # bulk create   # 4 inserts--
    db.session.commit()

'''
https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

        uselist--> one liner
        backref
        nullable
        lazy
        https://flask-sqlalchemy.palletsprojects.com/en/2.x/#api-reference  -- ORM Tutorial
        


Python --> 
    Flask --> web application  [code [python madhe]] ---> web application [db [flask_al],sms[lib],[pdf]]
'''