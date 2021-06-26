from db import db
from flask import session

def add_customer(name,email):
    if name == "" or email == "":
        return "Täytä kaikki kentät."
    if len(name) > 50 or len(email) >50:
        return "Nimi tai sähköposti liian pitkä."
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
    sql = "SELECT name, email, id FROM customers WHERE visible=1 ORDER BY name"
    result = db.session.execute(sql)
    customers = result.fetchall()
    return customers


def delete_customer(customer_id):
    sql = "UPDATE customers SET visible = 0 WHERE id = :customer_id"
    db.session.execute(sql, {"id":customer_id})
    db.session.commit()
    
