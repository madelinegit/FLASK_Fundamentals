from flask_app import app#new for CRUD, app didnt autofill
from flask import request, render_template, redirect, session
from flask_app.models.models_order import Order #from burger import Burger

@app.route('/')
def index():
    # users = User.get_all()
    return render_template('index.html', orders=Order.get_all())


#CREATE NEW ORDER PAGE ROUTE
@app.route('/order/new')
def new_order_page():
    return render_template("/new_order.html", orders=Order.get_all())

#CREATE: TAKES FORM TO DB
@app.route('/order/create', methods=['POST'])
def create_order():
    print(request.form)
    data = {
        'name' : request.form['name'],
        'cookie_type' : request.form['cookie_type'],
        'quantity' : request.form['quantity'],
    }
    # Order.create(data)
    print(data)
    return redirect('/')


#READ (reading one for show user page)
@app.route('/order/edit/<int:order_id>')
def show_edit_page(id): #tell it to expect dojo_id
    order_data = {
        'id' : request.form['id'],
        'name' : request.form['name'],
        'cookie_type' : request.form['cookie_type'],
        'quantity' : request.form['quantity'],
        "created_at": request.form['orders.created_at'],
        "updated_at": request.form['orders.updated_at'],
    }
    # all_ninjas=Ninja.get_all(data)
    one_order=Order.get_one(order_data)
    print(order_data)
    return render_template('edit_order.html', one_order=one_order)



#dojo(or ninja)/new(create)  / read(get) / delete() /update
#down the root of the tree


