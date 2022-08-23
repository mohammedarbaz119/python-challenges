
from distutils.log import error
from flask import Flask,render_template,redirect,request
import os
from pymongo import MongoClient
app = Flask(__name__)
connection = MongoClient('mongodb://localhost:27017/arbaz')
print(connection)
db = connection['arbaz']



@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/login',methods=['GET',"POST"])
def login():
    if(request.method=="GET"):
        return render_template('login.html')
    if(request.method=="POST"):
        name=request.form["name"]
        password = request.form["pass"]
        user =db.new.find_one({"name":name})
        if(user):
            return render_template('index.html',name=user['name'])
        else:
            return render_template('login.html',error="wrong details")
    



if __name__== '__main__':
    port = int(os.environ.get('PORT',3000))
    app.run(port=port,debug=True,host='0.0.0.0')