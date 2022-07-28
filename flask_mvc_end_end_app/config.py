from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/ormdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)


'''
prerquisites..
        stepone -->     D:\python_work\webdjenv\Scripts\            --> make sure kara--> Flask install ahe
                        right click on file and then simply --> give instruction --> pip install modulename

'''