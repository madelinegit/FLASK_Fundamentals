from flask import Flask, request, render_template, redirect
from Users import user
app=Flask(__name__)

# @app.route('/')
# def index():
#     users= user.get_all()
#     return render_template('index.html', users=user)

@app.route('/new_user')
def add_item():
    return render_template('/add_user.html')

@app.route('/success', methods=['POST'])
def success():
    print(request.form)
    data = {
        'first_name' : request.form['first_name'],
        'last_Name' : request.form['last_name'],
        'email' : request.form['email']
    }
    User.create(data)
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)