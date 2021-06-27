from app import app
from werkzeug.security import check_password_hash, generate_password_hash
from flask import redirect, render_template, request, session, abort
from db import db
import device, rent
import users, customers, service

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
        return render_template("login_error.html", message="Virheellinen käyttäjätunnus tai salsana")
    
    
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
        return render_template("login_error.html", message=message)


@app.route("/main_page", methods=["GET"])
def mainPage():
    devices = device.device_count()
    customer_count = customers.customer_count()
    return render_template("main_page.html", devices = devices, customers = customer_count)


@app.route("/customer")
def customer():
    all_customers = customers.get_customers()
    return render_template("customer.html", customers = all_customers)


@app.route("/add_customer", methods=["POST"])
def add_customer():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    name = request.form["name"]
    email = request.form["email"]
    message = customers.add_customer(name,email)
    if message=="1":
        return redirect("/customer")
    else:
        return render_template("error.html", message=message)
     

@app.route("/devices")
def devices():
    all_devices = device.get_devices()
    return render_template("devices.html", devices = all_devices)


@app.route("/add_device", methods=["POST"])
def add_device():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    device_type = request.form["device_type"]
    model = request.form["model"]
    description = request.form["description"]
    message = device.add_device(device_type,model,description)
    if message == "1":
        return redirect("/devices")
    else:
        return render_template("error.html", message=message) 
    
    
@app.route("/add_rent", methods=["POST"])
def rent_device():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    device_id = request.form["device_id"]
    customer_id = request.form["customer_id"]
    start_date = request.form["start_date"]
    end_date = request.form["end_date"]
    message = rent.rent_device(device_id, customer_id, start_date, end_date)
    if(message=="1"):
        return redirect("/rents")
    else:
        return render_template("error.html", message=message)
        


@app.route("/rents", methods=["GET", "POST"])
def rents():
    devices = device.get_devices()
    all_customers = customers.get_customers()
    all_rents = rent.get_rents()
    return render_template("/rents.html", devices = devices, customers = all_customers, rents = all_rents)


@app.route("/services", methods=["GET", "POST"])
def services():
    devices = device.get_devices()
    services = service.get_services()
    return render_template("/add_service.html", devices = devices, services = services)


@app.route("/add_service", methods=["GET", "POST"])
def add_service():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    device_id = request.form["device_id"]
    service_date = request.form["service_date"]
    description = request.form["description"]
    message = service.add_service(device_id, service_date, description)
    if message == "1":
        return redirect("/services")
    else: 
        return render_template("error.html", message = message)
    
