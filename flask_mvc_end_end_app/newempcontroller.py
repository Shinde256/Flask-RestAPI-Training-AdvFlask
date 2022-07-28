from flask_mvc_end_end_app.config import app,db
from flask import request,render_template
from flask_mvc_end_end_app.models import Employee

@app.route('/',methods = ['GET'])
def welcome_page():
    return render_template('employee.html',emplist = Employee.query.all())

@app.route('/save',methods = ['POST'])
def save_employee_info():
    formdata = request.form
    msg = None
    eid = int(formdata.get('id'))

    dbemp = Employee.query.filter_by(id=eid).first()        #
    if dbemp:       # if already present
        dbemp.name = formdata.get('name')
        dbemp.mobile = formdata.get('mobile')
        db.session.commit()     # update  --> u can write all other fields
        msg = 'Record Updated Successfully...!'
    else:
        #create new one
        emp = Employee(id = formdata.get('id'),
                       name= formdata.get('name'), mobile= formdata.get('mobile'), gender= formdata.get('gender'),
                       roles= formdata.get('roles'), address= formdata.get('address'), exp= formdata.get('exp'),
                       salary= formdata.get('salary'), skills= formdata.get('skills'))
        db.session.add(emp)
        db.session.commit()     # will fire insert query
        msg = 'Record Created Successfully...!'

    return render_template('employee.html',resp = msg,emplist = Employee.query.all())


@app.route('/',methods = ['GET'])
def edit_employee_info():
    return render_template('employee.html')


@app.route('/',methods = ['GET'])
def delete_emp_record():
    return render_template('employee.html')

if __name__ == '__main__':
    app.run(debug=True)