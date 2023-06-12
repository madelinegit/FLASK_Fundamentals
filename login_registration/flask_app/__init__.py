from flask import Flask
#no need to import flash or session
#just import flask
app= Flask(__name__)

app.secret_key = "PyPy 3.14"