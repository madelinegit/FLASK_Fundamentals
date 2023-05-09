from flask import Flask, render_template, request, redirect
from bank_model import Bank
app = Flask(__name__)
app.secret_key="i love database"

@app.route("/")
def index():
    # banks = Bank.get.all()
    return render_template("index.html", banks= Bank.get_all)

@app.route("/create_bank")
def show_create_bank_page():
    return render_template("create_bank.html")

@app.route("/create_bank", methods=["post"])
def create_bank():
    print(request.form)
    data= {
        'name' : request.form['name'],
        'address' : request.form['address'],
        'phone' : request.form['phone']
    }
    Bank.save(data) #saves the dctionary we just created
    return redirect("/")

@app.route("/show_bank/<int:id>")
def show_single_bank(id):
    bank = Bank.get_one(id)
    return render_template('display_one_bank.html')

if __name__ == "__main__":
    app.run(debug=True)
