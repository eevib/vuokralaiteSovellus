from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash

app=Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    sql = "SELECT password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None:
        return render_template("error.html", message="Virheellinen käyttjätunnus tai salasana")
    else: 
        hash_value = user[0]
        if check_password_hash(hash_value,password):
    	    session["username"] = username
        return redirect("/mainPage")
    
    
@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/newUser")
def newUser():
    return render_template("newUser.html")

@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    if len(password) < 3 or len(username) < 3: 
         return render_template("error.html", message="Käyttäjätunnus ja salasana on oltava vähintään 3 merkkiä pitkä.")
    else: 
        hash_value = generate_password_hash(password)
        sql = "INSERT INTO users (username,password) VALUES (:username, :password)"
        db.session.execute(sql, {"username":username,"password":hash_value})
        db.session.commit()
    return redirect("/")

@app.route("/mainPage")
def mainPage():
    return render_template("mainPage.html")

@app.route("/customer")
def customer():
    return render_template("customer.html")

@app.route("/addCustomer", methods=["POST"])
def addCustomer():
    name = request.form["name"]
    email = request.form["email"]
    sql = "INSERT INTO customers (name,email) VALUES (:name, :email)"
    db.session.execute(sql, {"name":name,"email":email})
    db.session.commit()
    return redirect("/mainPage")
