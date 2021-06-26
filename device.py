from db import db
from flask import session


def add_device(device_type, model, description):
    if device_type == "" or model == "":
        return "Täytä ainakin kentät tyyppi ja malli."
    if len(device_type) > 50 or len(model) > 50 or len(description) > 300:
        return "Tyypin ja mallin suurimmat sallitut pituudet ovat 50 merkkiä ja kuvauksen 300 merkkiä."
    sql = "INSERT INTO devices (device_type, model, description) VALUES (:device_type, :model, :description)"
    db.session.execute(sql, {"device_type":device_type, "model":model, "description":description})
    db.session.commit()
    return "1"
    
    
def get_devices():
    sql = "SELECT * from devices ORDER BY model, device_type"
    result = db.session.execute(sql)
    devices = result.fetchall()
    return devices  
