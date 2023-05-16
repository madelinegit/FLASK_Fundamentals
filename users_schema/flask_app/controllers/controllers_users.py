from flask_app import app#new for CRUD, app didnt autofill
from flask import request, render_template, redirect, session
from flask_app.models.models_user import User #from burger import Burger


@app.route('/users')
def index():
    # users = User.get_all()
    return render_template('users.html', users=User.get_all())

# @app.route('/users')
# def users():
#     return render_template("users.html", users=User.get_all())
#identical funcitons?
#gets all the stuff via OOP

#CREATE NEW USER PAGE ROUTE
@app.route('/user/new')
def new_user_page():
    return render_template("/new_user.html")

#CREATE: TAKES FORM TO DB
@app.route('/user/new', methods=['POST'])
def create_user():
    print(request.form)
    data = {
        'firstname' : request.form['firstname'],
        'lastname' : request.form['lastname'],
        'email' : request.form['email']
    }
    User.create(data)
    return redirect('/users')

#READ (reading one user for the edit page)
@app.route('/user/edit/<int:user_id>')
def edit_user_page(user_id): #tell it to expect user_id
    data = {
        'id' : user_id,
    }
    one_user=User.get_one(data)
    return render_template('edit_user.html', one_user=one_user)
#it needs to be told to pull the user_id defined as part of the dictionary


#UPDATE this tells the database the new information on the way to the page that shows us what we just did
@app.route('/user/update/<int:user_id>', methods=['POST'])
def update_user(user_id):
    # user=User.get_one(id)
    print(request.form)
    data = {
        # 'id' : user_id,
        'firstname' : request.form['firstname'],
        'lastname' : request.form['lastname'],
        'email' : request.form['email']
    }
    User.update(data, user_id)
    return redirect('/users')


if __name__=="__main__":
    app.run(debug=True)
