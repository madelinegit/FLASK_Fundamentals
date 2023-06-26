from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.models_user import User
from flask_app.models.models_car import Car
from flask_app.config.mysqlconnection import connectToMySQL
# from datetime import date

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    user_data = {
        'id' : session ['user_id']
        }
    user = User.get_one(user_data)
    all_cars = Car.get_all_cars_with_user()
    # one_seller=Car.get_all_cars_with_user()
    print("ALL_CARS:", all_cars)
    return render_template ('dashboard.html', user=user, all_cars=all_cars)
# one_seller=one_seller

@app.route('/create')
def create():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('car_create.html')
    #return redirect('/create')

@app.route("/car_create", methods=["POST"])
def car_create():
    print("REQUEST.FORM", request.form)
    isValid=Car.car_validate(request.form)
    if not isValid:
        print('HEY! ISVALID=FALSE <3')
        flash('Please try again.')
        return redirect('/create')
    if isValid:
        print("VALID LISTING")
    newdata = {
    'price' : request.form['price'],
    'model' : request.form['model'],
    'make' : request.form['make'],
    'year' : request.form['year'],
    'description' : ['description'],
    'user_id' : session['user_id']
    }
    print("NEWDATA: ", newdata)
    id=Car.car_create(newdata)
    print("LISTING SAVED")
    return redirect('/dashboard')

#Read
@app.route('/car_view/<int:id>')
def car_view(id):
    if 'user_id' not in session:
        return redirect('/')
    car_data = { 'id' : id }
    car=Car.get_one_car(car_data)
    user_data = { 'id' : session['user_id'] }
    user=User.get_one(user_data)
    print("CAR:", car)
    print("CAR_DATA: ", car_data)
    return render_template('car_view.html', car=car, user=user)
#user part not necessary unless rendering logged in user in jinja, user=user
#here I edited it in to hack around the fact that my get one join didn't work.

#Read/Update Page
@app.route('/car_edit/<int:id>')
def car_edit(id):
    if 'user_id' not in session:
        return redirect('/')
    car_data = { 'id' : id }
    car=Car.get_one_car(car_data)
    user_data = { 'id' : id }
    user=User.get_one(user_data)
    print("CAR:", car)
    print("CAR_DATA: ", car_data)
    return render_template('car_edit.html', car=car, user=user)

#Update
@app.route('/car_update/<int:id>', methods=["POST"])
def car_update(id):
    isValid=Car.car_validate(request.form)
    if not isValid:
        print("INVALID ENTRY")
        flash("Input Not Valid.")
        return redirect(f'/car_edit/{id}')
    Car.update(request.form, id)
    return redirect('/dashboard')

#Delete
@app.route('/car_destroy/<int:id>')
def car_destroy(id):
    data = { 'id' : id }
    Car.delete(data)
    flash("Car was just deleted.")
    return redirect('/dashboard')