from db import db

def rent_device(device_id, customer_id, start_day, end_day):
    if(device_id == "" or customer_id == "" or start_day == "" or end_day == ""):
        return "Täytä kaikki kentät."
    sql = "SELECT 1 FROM devices WHERE id=:id"
    result = db.session.execute(sql, {"id":device_id})
    device = result.fetchone()
    sql = "SELECT 1 FROM customers WHERE id=:id"
    result = db.session.execute(sql, {"id":customer_id})
    customer = result.fetchone()
    
    if(device==None):
        return "Laitetta ei löydy."
    elif(customer==None):
        return "Asiakasta ei löydy."
    else:
        sql = "INSERT INTO rents (customer_id, device_id, start_day, end_day) VALUES (:customer_id, :device_id, :start_day, :end_day)"
        db.session.execute(sql, {"customer_id":customer_id, "device_id":device_id, "start_day":start_day, "end_day":end_day})
        db.session.commit()
        return "1"
    
    
def get_rents():
    sql = "SELECT C.name, C.email, R.start_day, R.end_day, D.model, D.id FROM customers C, rents R, devices D WHERE R.customer_id=C.id AND R.device_id=D.id ORDER BY end_day"
    result = db.session.execute(sql)
    rents = result.fetchall()
    return rents
