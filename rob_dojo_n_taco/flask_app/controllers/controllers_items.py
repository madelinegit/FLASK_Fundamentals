from flask_app import app
from flask import request, render_template, redirect
from flask_app.models.models_item import Item

@app.route('/')
def index():
    pineapple = Item.get_all()
    return render_template('index.html', items = pineapple)

# New Item Page
@app.route('/new_menu_item')
def new_menu_item():
    return render_template('add_item.html')

# Add Item
@app.route('/success', methods=['POST'])
def success():
    data = {
        'food_item' : request.form['food_item'],
        'description' : request.form['description'],
        'price' : request.form['price']
    }
    Item.create(data)
    return redirect('/')

# Update Item Page
@app.route('/edit/<int:item_id>')
def update_item(item_id):
    data = {
        'id' : item_id
    }
    item = Item.get_one(data)
    return render_template('edit_item.html', item = item)

# Updated Item
@app.route('/update/<int:item_id>', methods=['POST'])
def updated_item(item_id):
    # data = {
    #     'id' : item_id,
    #     'food_item' : request.form['food_item'],
    #     'description' : request.form['description'],
    #     'price' : request.form['price']
    # }
    Item.update(request.form, item_id)
    return redirect('/')

# Delete Item
@app.route('/delete/<int:item_id>')
def delete(item_id):
    data = {'id': item_id}
    Item.delete(data)
    return redirect('/')