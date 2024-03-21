from flask import Flask, render_template, request
from pymongo import MongoClient

cluster=MongoClient('mongodb+srv://syamdamarla7:syamkumar123@cluster0.9cyvv4g.mongodb.net/')
db=cluster['registration']
collection=db['users']

app=Flask(__name__)

@app.route('/menu')
def main():
    return render_template('menuBox.html')

@app.route('/')
def best():
    return render_template('best_recipe.html')

@app.route('/about')
def about():
    return render_template('aboutUs.html')

@app.route('/cal')
def cal():
    return render_template('calendar.html')


@app.route('/login')
def login():
    return render_template('login_form.html')

@app.route('/register')
def signup():
    return render_template('register_form.html')


@app.route('/contact')
def Contact():
    return render_template('contact_us.html')



@app.route('/userreg',methods=['post'])
def reg():
    name=request.form['name']
    email=request.form['email']
    password=request.form['password']
    collection.insert_one({ "name":name,"email":email,"password":password})
    return render_template('login_form.html')


@app.route('/loginuser', methods=['post'])
def log():
    name=request.form['name']
    password=request.form['password']
    data=collection.find_one({"name":name})
    print(type(data))
    if data:
        if data['name']==name and data['password']==password:
            return render_template('front_page.html')
        else:
            return render_template('login_form.html', status="wrong credentials")
    else:
        return render_template('login_form.html',status="user not found")





if(__name__=='__main__'):
    app.run(debug=True)