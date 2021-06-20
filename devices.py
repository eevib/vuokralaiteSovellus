from db import db
from flask import session


def add_device(device_type, model, description):
    sql = "INSERT INTO devices (device_type, model, description) VALUES (:device_type, :model, :description)"
    db.session.execute(sql, {"device_type":device_type, "model":model, "description":description})
    db.session.commit()
    
    
def get_devices():
    sql = "SELECT * from devices"
    result = db.session.execute(sql)
    devices = result.fetchall()
    return devices  
