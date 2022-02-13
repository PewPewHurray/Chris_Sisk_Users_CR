from flask import Flask, render_template, request, redirect
app = Flask(__name__)
app.secret_key="one key to rule them all"

import sys

from user import User

@app.route("/")
def to_users():

    return render_template("users.html")

@app.route("/users")
def users():

    users = User.get_all()
    print(users)

    return render_template("users.html", all_users = users)

@app.route("/new_user")
def new_user():

    return render_template("new_user.html")

@app.route("/add_user", methods=["POST"])
def add_user():

    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }

    User.save(data)

    return redirect("/users")

if __name__=="__main__":
    app.run(debug=True)