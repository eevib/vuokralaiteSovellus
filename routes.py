from app import app
from werkzeug.security import check_password_hash, generate_password_hash
from flask import redirect, render_template, request, session
from db import db
import users

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if users.login(username,password):
        return redirect("/main_page")
    else: 
        return render_template("error.html", message="Virheellinen käyttäjätunnus tai salsana")
    
    
@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/new_user")
def newUser():
    return render_template("new_user.html")

@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    message=users.register(username,password)
    if message=="1":
        return redirect("/main_page")
    else:
        return render_template("error.html", message=message)

@app.route("/main_page", methods=["GET"])
def mainPage():
    sql = "SELECT * from customers"
    result = db.session.execute(sql)
    customers = result.fetchall()
    sql = "SELECT * from devices"
    result = db.session.execute(sql)
    devices = result.fetchall()
    return render_template("main_page.html", customers=customers,devices=devices)

@app.route("/customer")
def customer():
    return render_template("customer.html")

@app.route("/add_customer", methods=["POST"])
def addCustomer():
    name = request.form["name"]
    email = request.form["email"]
    sql = "SELECT email FROM customers WHERE email=:email"
    result = db.session.execute(sql, {"email":email})
    customer = result.fetchone()
    if customer == None:
        sql = "INSERT INTO customers (name,email) VALUES (:name, :email)"
        db.session.execute(sql, {"name":name,"email":email})
        db.session.commit()
        return redirect("/main_page")
    else:
        return render_template("error.html", message="Asiakas on jo olemassa")
     

@app.route("/devices")
def devices():
    return render_template("devices.html")

@app.route("/add_device", methods=["POST"])
def add_device():
    device_type = request.form["device_type"]
    model = request.form["model"]
    description = request.form["description"]
    sql = "INSERT INTO devices (device_type,model,description) VALUES (:device_type, :model, :description)"
    db.session.execute(sql, {"device_type":device_type,"model":model,"description":description})
    db.session.commit()
    return redirect("/main_page")
    
    
@app.route("/add_rent", methods=["POST"])
def rent_device():
    return redirect("/main_page")
