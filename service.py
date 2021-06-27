from db import db

def add_service(device_id, service_date, description):
    if device_id == "" or service_date == "" or description == "":
        return "Täytä kaikki kentät."
    elif len(description) > 300:
        return "Kuvauksen maksimipituus on 300"    
    sql = "SELECT 1 FROM devices WHERE id=:id"
    result = db.session.execute(sql, {"id":device_id})
    device = result.fetchone()
    if device == None:
        return "Laitetta ei löydy."
    sql = "INSERT INTO services (device_id, service_date, description, visible) VALUES (:device_id, :service_date, :description, 1)"
    db.session.execute(sql, {"device_id":device_id, "service_date":service_date, "description":description})
    db.session.commit()
    return "1"

def get_services():
    sql = "SELECT D.id, D.device_type, D.model, S.service_date, S.description FROM devices D, services S WHERE S.device_id = D.id AND S.visible = 1"
    result = db.session.execute(sql)
    services = result.fetchall()
    return services
    
