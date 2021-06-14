from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username,password):
    sql = "SELECT password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None:
        return False
    else: 
        hash_value = user[0]
        if check_password_hash(hash_value,password):
    	    session["username"] = username
    	    return True
        else:
            return False
        
def register(username,password):
    sql = "SELECT password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    users = len(result.fetchall())
    if users > 0:
        return "Käyttäjätunnus on jo käytössä, valitse toinen."
    if len(password) < 3 or len(username) < 3 or len(password) > 20 or len(username) > 20: 
        return "Käyttäjätunnus ja salasana on oltava vähintään 3 merkkiä pitkiä ja saavat olla enintään 20 merkkiä pitkät."
    else: 
        hash_value = generate_password_hash(password)
        sql = "INSERT INTO users (username,password) VALUES (:username, :password)"
        db.session.execute(sql, {"username":username,"password":hash_value})
        db.session.commit()
        session["username"] = username
    return "1"
    
