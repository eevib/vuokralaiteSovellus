from db import db

def rent_device(device_id, customer_id, start_day, end_day):
    sql = "INSERT INTO rents (customer_id, device_id, start_day, end_day) VALUES (:customer_id, :device_id, :start_day, :end_day)"
    db.session.execute(sql, {"customer_id":customer_id, "device_id":device_id, "start_day":start_day, "end_day":end_day})
    db.session.commit()
    
    
def get_rents():
    sql = "SELECT * FROM rents"
    result = db.session.execute(sql)
    rents = result.fetchall()
    return rents


def get_ordered_rents():
    sql = "SELECT "
