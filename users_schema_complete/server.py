# from flask_app import app
# from flask import render_template, redirect, reqest, session

from flask_app import app
# from flask_app.models.models_user import User
from flask_app.controllers import controllers_users

# from user import User
#from (place) import (thing)

#should there be a create route here?




if __name__=="__main__":
    app.run(debug=True)

#Go thru modularization apges in the platform