from operator import concat
from flask import Flask, render_template, request, redirect, url_for
import os # importing operating system module
app = Flask(__name__)
# to stop caching static file
# def getdict(n:list):
def calc(n:list):
    dict ={}
    
    newlist = list(map(lambda x : x.strip(),n))
    for x in newlist:
        dict.update({x:newlist.count(x)})

    print(dict)
    return dict


app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.route('/') # this decorator create the home route
def home ():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = "Text analyser"
    return render_template('index.html', techs=techs, name = name, title = 'Home')

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name = name, title = 'About Us')

@app.route('/result',methods=['POST'])
def result():
    if(request.method=="POST"):
        
        cool = request.form['content'].split(' ')
        dict =calc(cool)
        le = len(cool)
        len_string=len(request.form['content'])

        return render_template('result.html',cool=le,dict=dict,char=len_string)

    
@app.route('/post', methods= ['GET','POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
         return render_template('post.html', name = name, title = name)
    if request.method =='POST':
        content = request.form['content']
        print(content)
        return redirect(url_for('result'))


if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)