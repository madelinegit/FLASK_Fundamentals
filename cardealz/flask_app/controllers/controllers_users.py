from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.models_user import User
from flask_app.models.models_car import Car
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login_user', methods = ["post"])
def login_user():
    data = {
        'email' : request.form['email'],
    }
    user = User.get_email(data)
    if not user:
        flash("That email is not in the database register.")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash ("Wrong Password")
        print(request.form['password'])
        print(user.password)
        return redirect('/')
    else:
        session['user_id'] = user.id
        # ^ calls ID from dictionary
        # flash("optional, didn't look that cool")
        print('in session')
        return redirect ('/dashboard')

@app.route('/register', methods=['post'])
def register():
    isValid=User.validate(request.form)
    if not isValid:
        return redirect('/')
    else:
        newdata = {
            'firstname' : request.form['firstname'],
            'lastname' : request.form['lastname'],
            'email' : request.form['email'],
            'password' : bcrypt.generate_password_hash(request.form['password']),
            # 'confirm_password' : bcrypt.generate_password_hash(request.form['confirm_password'])
        }
        id = User.create_new_user(newdata)
        print("user saved")
        if not id:
            flash("something went wrong")
            return redirect('/')
        else:
            session['user_id'] = id #here I defined user_id
            print("login successful")
            return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    flash("Logged Out")
    return redirect('/')