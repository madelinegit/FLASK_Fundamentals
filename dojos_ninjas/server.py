from flask_app import app
from flask_app.controllers import controllers_ninjas, controllers_dojos

if __name__=="__main__":
    app.run(debug=True)