from flask_app import app
from flask import Flask, render_template, request, redirect
from flask_app.model.models_user import User

app=Flask(__name__)

@app.route('/')
def users():
    return render_template("users.html",users= User.get_all())

@app.route('/user/new')
def new():
    return render_template("new_user.html")

@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/')

@app.route('/user/show/<int:user_id>')
def show(user_id):
    data = {"id":user_id}
    return render_template('show_users.html',user= User.get_one(data))

@app.route('/user/edit/<int:user_id>')
def edit(user_id):
    data = {"id":user_id}
    return render_template('edit_user.html', user= User.get_one(data))

@app.route('/user/update/<int:user_id>', methods=['POST'])
def update(user_id):
    # data = {"id":user_id} 
    User.update(request.form, user_id)
    return redirect ('/')

@app.route('/user/delete/<int:user_id>')
def delete(user_id):
    data = {"id":user_id}
    User.delete(data)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)