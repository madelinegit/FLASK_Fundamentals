from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.models_users import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if 'user_id' not in session:
        return render_template('index.html')
    else:
        return render_template('welcome.html')

@app.route('/welcome')#<user_id>, int:user_id
def welcome():
    if 'user_id' not in session:
        return redirect('/')
    else:
        data= {
            'id' : session['user_id']
            }
        one_user=User.get_one(data)
        return render_template('welcome.html', one_user=one_user)

#one_user=User.get_one(data))
# @app.route('/login', methods=['POST'])
# def login():
#     return redirect('/welcome')
#CREATE POST/ TO WELCOME PAGE ROUTE

@app.route('/register', methods=['post'])
def register():
    isValid=User.validate(request.form)
    if not isValid:
        return redirect('/')
    else:
        newdata = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'password' : bcrypt.generate_password_hash(request.form['password'])
        }
        id = User.save(newdata)
        if not id:
            flash("something went wrong")
            return redirect('/')
        else:
            session['user_id'] = id #here I defined user_id
            flash ("login successful")
            return redirect('/welcome')

#READ/ WELCOME PAGE ROUTE (getting one)
@app.route('/login', methods = ["post"])
def login(): #user_id variable created here
    data = {
        'email' : request.form['email'],
    }
    user = User.getEmail(data)
    if not user:
        flash("That email is not in the database register.")
        redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash ("Wrong Password")
        print(request.form['password'])
        print(user.password)
        return redirect('/')
    else:
        session['user_id'] = user.id #it got us a whole dictionary, and now we are calling on just the ID
        flash("welcome back")
        return redirect ('/welcome')

@app.route('/logout')
def logout():
    session.clear()
    flash("Byeee")
    return redirect('/')
