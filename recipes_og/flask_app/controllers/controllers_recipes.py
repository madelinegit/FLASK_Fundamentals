from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.models_user import User
from flask_app.models.models_recipe import Recipe
from flask_app.config.mysqlconnection import connectToMySQL
# from datetime import date
# bcrypt = Bcrypt(app)

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    user_data = {
        'id' : session ['user_id']
        }
    user = User.get_one(user_data)
    all_recipes = Recipe.get_all()
    # thirtymin_string = request.form.get('thirtymin', "0")
    print("all_recipes:", all_recipes)
    return render_template('recipe_dashboard.html', user=user, all_recipes=all_recipes)

@app.route('/create')
def create():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('recipe_create.html')

@app.route("/recipe_create", methods=["POST"])
def recipe_create():
    print("request.form", request.form)
    isValid=Recipe.recipe_validate(request.form)
    if not isValid:
        return redirect('/recipe_create')
    # else:
    if 'thirtymin' in request.form:
        newdata = {
            'name' : request.form['name'],
            'description' : request.form['description'],
            'instructions' : request.form['instructions'],
            'datecreated' : request.form['datecreated'],
            'thirtymin' : request.form['thirtymin'],
            'user_id' : session['user_id']
        }
    else:
        newdata = {
        'name' : request.form['name'],
        'description' : request.form['description'],
        'instructions' : request.form['instructions'],
        'datecreated' : request.form['datecreated'],
        'thirtymin' : ['No'],
        'user_id' : session['user_id']
        }
    id=Recipe.recipe_create(newdata)
    print("recipe saved")
    return redirect('/dashboard')

@app.route('/recipe_read/<int:id>')
def recipe_read(id):
    recipe_data = {
        'id' : id
    }
    user_data = {
        'id' : session ['user_id']
        }
    user = User.get_one(user_data)
    # user=User.get_one({"id":session['user_id']})
    # #the ID's seem to match but they dont (same as last 3 lines)
    recipe=Recipe.get_one_chef_with_recipe(recipe_data)
    # print(user) user=user
    return render_template('recipe_read.html', user=user, recipe=recipe)

@app.route('/recipe_edit/<int:id>')
def recipe_read_edit(id):
    if 'user_id' not in session:
        return redirect('/')
    recipe_data = {
        'id' : id
    }
    user_data = {
        'id' : session ['user_id']
    }
    user=User.get_one(user_data)
    recipe=Recipe.get_one_chef_with_recipe(recipe_data)
    print("user: ", user)
    return render_template('recipe_update.html', user=user, recipe=recipe)

@app.route('/recipe_update/<int:id>', methods = ["POST"])
def recipe_update(id):
    # if 'user_id' not in session:
    #     return redirect('/')
    # print("request.form", request.form)
    # print("id: ", id)
    isValid=Recipe.recipe_validate(request.form)
    if not isValid:
        flash("Input not valid.")
        return redirect(f'/recipe_edit/{id}')
    # recipe = Recipe.get_one(data)  recipe=recipe """
    Recipe.update(request.form, id)
    return redirect('/dashboard')

@app.route('/recipe_delete/<int:id>')
def recipe_delete(id):
    data = {
        "id" : id
    }
    Recipe.delete(data)
    flash("Selected recipe has been deleted.")
    return redirect('/dashboard')



