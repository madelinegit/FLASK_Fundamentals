from flask_app import app #new for CRUD, go to flask_app
from flask import request, render_template, redirect
# from flask_app.models.models_item import Item #new location i put in manually

from flask_app.models.models_item import Item

@app.route('/')
def index():
    pineapple= Item.get_all()
    return render_template('index.html', items=pineapple)
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

#Update Item Page
@app.route('/edit/<int:item_id>')
def update_item(item_id):
    data = {
        'id' : item_id
    }
    item=Item.get_one(data)
    return render_template('edit_item.html', item=item)

#Updated Item
@app.route('/update/<int:item_id>', methods=['POST']) #post updates the form
def updated_item(item_id):
    Item.update(request.form, item_id)
    return redirect('/')
    """ data= {
        'id' : item_id,
        'fooditem' : request.form['fooditem'],
        'description' : request.form['description']
    }
    Item.update(data) DOES THE SAME THING!"""




#there should be no app.run at the end of this doc