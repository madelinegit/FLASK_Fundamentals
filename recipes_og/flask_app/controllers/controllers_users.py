from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.models_user import User
from flask_app.models.models_recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def login():
    # if 'user_id' in session:
    #     return render_template('recipe_dashboard.html')
    # didnt work?
    return render_template('login.html')

# @app.route('/dashboard')
# def show_user():
#     if 'user_id' not in session:
#         return redirect('/')
#     else:
#         data= {
#             'id' : session['user_id']
#             # 'id' : user_id
#             }
#         one_user=User.get_one(data)
#         recipes = Recipe.get_all(data)
#         return render_template('recipe_dashboard.html', one_user=one_user, recipes=recipes)

@app.route('/login_user', methods = ["post"])
def login_user(): #user_id variable created here
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
        session['user_id'] = user.id
        # ^ it got us a whole dictionary, and now we are calling on just the ID
        flash("welcome back")
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
        id = User.save(newdata)
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
