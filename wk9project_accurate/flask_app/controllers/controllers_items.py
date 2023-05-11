from flask_app import app #new for CRUD, go to flask_app
from flask import request, render_template, redirect
# from flask_app.models.models_item import Item #new location i put in manually

from flask_app.models.models_item import Item

@app.route('/')
def index():
    items= Item.get_all()
    return render_template('index.html', items=items)
#capitalizd was refering to a class & caused a bug

@app.route('/new_menu_item')
def add_item():
    return render_template('/add_item.html')

#Add Item
@app.route('/success', methods=['POST'])
def success():
    # print(request.form)
    data = {
        # 'fooditem' : request.form['fooditem'],
        'fooditem' : request.form['fooditem'],
        'description' : request.form['description']
    }
    Item.create(data)
    return redirect('/')

#Update Item
@app.route('/update/<int:item_id>', methods=['POST'])
def update_item(item, id):
    return render_template('edit_item.html')
    pass

#there should be no app.run at the end of this doc