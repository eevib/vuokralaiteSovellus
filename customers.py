from db import db
from flask import session

def add_customer(name,email):
    sql = "SELECT email FROM customers WHERE email=:email"
    result = db.session.execute(sql, {"email":email})
    customer = result.fetchone()
    if customer == None:
        sql = "INSERT INTO customers (name,email) VALUES (:name, :email)"
        db.session.execute(sql, {"name":name, "email":email})
        db.session.commit()
        return "1"
    else:
        return "Asiakas on jo olemassa"
    
    
def get_customers():
    sql = "SELECT * from customers"
    result = db.session.execute(sql)
    customers = result.fetchall()
    return customers
    
     
