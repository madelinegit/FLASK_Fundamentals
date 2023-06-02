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
    Order.create_order(data)
    print(data)
    return redirect('/')


#READ/ EDIT PAGE ROUTE (getting one)
@app.route('/order/edit/<int:order_id>')
def show_edit_page(order_id): #tell it to expect dojo_id
    data = {
        'id' : order_id,
    }
    # all_ninjas=Ninja.get_all(data)
    one_order=Order.get_one(data)
    print(data)
    return render_template('edit_order.html', one_order=one_order)

#UPDATE/ TAKES FORM TO DB
@app.route('/order/update/<int:order_id>', methods=["POST"])
def update_order(order_id):
    Order.update_order(request.form, order_id)
    # print(order_id)
    """ order_id = {
        'id' : order_id,
        'name' : request.form['name'],
        'cookie_type' : request.form['cookie_type'],
        'quantity' : request.form['quantity'],
    } """
    return redirect('/')



