from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.property import Property
from flask_app.models.user import User

@app.route('/new/property')
def new_property():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id']
    }
    return render_template('new_property.html', user= User.get_by_id(data))

@app.route('/create/property', methods=['POST'])
def create_property():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Property.validate_property(request.form):
        return redirect('/new/property')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "information": request.form["information"],
        "under30": int(request.form["under30"]),
        "date_made": request.form["date_made"],
        "user_id": session["user_id"],
    }
    Property.save(data)
    return redirect('/dashboard')


@app.route('/destroy/property/<int:id>')
def destroy_property(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    clickedProperty = Property.get_one(data)
    print(clickedProperty)
    if clickedProperty['user_id'] == session['user_id']:
        Property.destroy(data)
        return redirect ('/dashboard')
    return redirect('/dashboard')


@app.route('/property/<int:id>')
def show_property(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    userData = {
        "id": session['user_id']
    }
    clickedProperty = Property.get_one(data)
    print(clickedProperty)
    return render_template('show_property.html', property = Property.get_one(data), user=User.get_by_id(userData))

@app.route('/edit/property/<int:id>')
def edit_property(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    userData = {
        "id": session['user_id']
    }
    return render_template('edit_property.html', edit = Property.get_one(data), user=User.get_by_id(userData))

@app.route('/update/property/', methods=['POST'])
def update_property():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Property.validate_property(request.form):
        return redirect(request.referrer)
    
    data = {
         "name": request.form["name"],
        "description": request.form["description"],
        "information": request.form["information"],
        "under30": int(request.form["under30"]),
        "date_made": request.form["date_made"],
        "id": request.form["id"],
    }
    Property.update(data)
    return redirect('/dashboard')

