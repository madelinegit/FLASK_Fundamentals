from flask_app import app#new for CRUD, app didnt autofill
from flask import request, render_template, redirect, session
from flask_app.models.models_ninja import Ninja #from burger import Burger
from flask_app.models.models_dojo import Dojo


#CREATE NEW USER PAGE ROUTE
@app.route('/new/ninja')
def new_ninja_page():
    return render_template("/new_ninja.html", dojos=Dojo.get_all())

#CREATE: TAKES FORM TO DB
@app.route('/new/ninja', methods=['POST'])
def create_ninja():
    print(request.form)
    data = {
        'dojo_id' : request.form['city_id'],
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age']
    }
    #those naming conventions, I could delete the second part after request form and just change the city_id to dojo_id in the HTML and no consequences
    Ninja.create(data)
    print(data)
    return redirect('/')

#READ (reading one for show user page)
@app.route('/ninjas/show/<int:dojo_id>')
def show_user_page(dojo_id): #tell it to expect dojo_id
    data = {
        'id' : dojo_id
    }
    all_ninjas=Ninja.get_all(data)
    return render_template('view_ninjas.html', ninjas=Ninja.get_all())


if __name__=="__main__":
    app.run(debug=True)