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
        return render_template("error.html", message="Virheellinen käyttäjätunnus")
    else: 
        hash_value = user[0]
        if check_password_hash(hash_value,password):
    	    session["username"] = username
    	    return redirect("/mainPage")
        else:
            return render_template("error.html", message="Virheellinen salasana")
        
    
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
    sql = "SELECT password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    users = len(result.fetchall())
    print(users)
    if users > 0:
        return render_template("error.html", message="Käyttäjätunnus on jo käytössä, valitse toinen.")
    if len(password) < 3 or len(username) < 3: 
         return render_template("error.html", message="Käyttäjätunnus ja salasana on oltava vähintään 3 merkkiä pitkä.")
    else: 
        hash_value = generate_password_hash(password)
        sql = "INSERT INTO users (username,password) VALUES (:username, :password)"
        db.session.execute(sql, {"username":username,"password":hash_value})
        db.session.commit()
        session["username"] = username
    return redirect("/mainPage")

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

@app.route("/devices")
def devices():
    return render_template("devices.html")

@app.route("/addDevice", methods=["POST"])
def addDevice():
#    deviceType = request.form["deviceType"]
#    model = request.form["model"]
#    description = request.form["description"]
#    sql = "INSERT INTO devices (deviceType,model,description) VALUES (:deviceType, :model, :description)"
#    db.session.execute(sql, {"deviceType":deviceType,"model":model,"description":description})
#    db.session.commit()
    return redirect("/mainPage")
    
