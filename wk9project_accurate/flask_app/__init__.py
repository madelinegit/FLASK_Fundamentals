from flask import Flask

app = Flask(__name__)
#new
app.secret_key = "Py is Life"
#this will get used in the next phase of coding