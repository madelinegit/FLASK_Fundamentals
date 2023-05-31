from flask_app import app#new for CRUD, app didnt autofill
from flask import request, render_template, redirect, session
from flask_app.models.models_ninja import Ninja #from burger import Burger
from flask_app.models.models_dojo import Dojo #from burger import Burger

@app.route('/')
def index():
    # users = User.get_all()
    return render_template('index.html', dojos=Dojo.get_all())

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

#READ (reading one for show user page)
@app.route('/ninjas/show/<int:dojo_id>')
def show_user_page(dojo_id): #tell it to expect dojo_id
    data = {
        'id' : dojo_id
    }
    # all_ninjas=Ninja.get_all(data)
    dojo=Dojo.get_one(data)
    print(dojo)
    return render_template('view_ninjas.html', dojo=dojo)



#dojo(or ninja)/new(create)  / read(get) / delete() /update
#down the root of the tree