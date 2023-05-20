from flask_app import app#new for CRUD, app didnt autofill
from flask import request, render_template, redirect, session
from flask_app.models.models_ninja import Ninja #from burger import Burger
from flask_app.models.models_dojo import Dojo #from burger import Burger

@app.route('/')
def index():
    # users = User.get_all()
    return render_template('index.html', dojos=Dojo.get_all())

#CREATE NEW DOJO PAGE ROUTE
# @app.route('/new/dojo')
# def new_dojo_page():
#     return render_template('/')

#CREATE: TAKES FORM TO DB
@app.route('/new/dojo', methods=['POST'])
def create_dojo():
    print(request.form)
    data = {
        'name' : request.form['name'],
    }
    Dojo.create(data)
    print(data)
    return redirect('/')
