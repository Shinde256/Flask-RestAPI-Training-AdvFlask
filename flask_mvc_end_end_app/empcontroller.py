from flask_mvc_end_end_app.config import app
from flask import request,render_template

                            #http://localhost:5000      ---> base uri
                            #localhost = 127.0.0.1  ---> 5000 --> flask chalu ahe
@app.route('/',methods=['GET'])             # bydefault method -- type is  --> GET      --> 127.0.0.1 ---localhost --windows/system32/drivers/etc/hosts-->
def welcome_page():
    print('inside welcome_page')
    print(request.args)         # this attribute retrives the data from ---> get method --which is mentioned inside form
   # return render_template('employee.html')
    return render_template('employee.html',data=[10,20,30,40])


@app.route('/',methods=['POST'])
def save_employee_info():
    print('inside save_employee_info')
    print(request.form)             # this attributes retrives the data from --> form post method -->
    return render_template('employee.html',data = [10,20,30,40])


@app.route('/index',methods=['POST','GET'])     #http://localhost:5000/index --> url -- enter ->get
def save_employee_info_both():                  #http://localhost:5000/index --> form --> no type mentioned-->get
    print('inside save_employee_info_both')          #http://localhost:5000/index --> form --> type mentioned:post-->get
    formdata = None
    if request.method == 'GET':
        print('data is inside get method -url')
        formdata = request.args
    else:
        print('data is inside post method request body')
        formdata = request.form
    print(formdata)             # this attributes retrives the data from --> form post method -->
    return render_template('employee.html')


if __name__ == '__main__':
    app.run(debug=True,port=8081)     #debug=True --> runtime changes accept karto
