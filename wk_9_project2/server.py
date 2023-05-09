from flask import Flask, request, render_template, redirect
from item import Item
app=Flask(__name__)

@app.route('/')
def index():
    items= Item.get_all()
    return render_template('index.html', items=Item)

@app.route('/new_menu_item')
def add_item():
    return render_template('/add_item.html')

@app.route('/success', methods=['POST'])
def success():
    print(request.form)
    data = {
        'food_item' : request.form['food_item'],
        'description' : request.form['description']
    }
    Item.create(data)
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)