from db import db
import users

def get_list():
    sql = "SELECT v.id, v.vacc, v.date, p.placename FROM vaccination v INNER JOIN place p ON p.id=v.place_id;"
    result = db.session.execute(sql)
    return result.fetchall()

def send(name,place,vacc,date):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO vaccination (vacc, place_id, date) VALUES (:vacc, (SELECT id FROM place WHERE placename=:place), :date)"
    db.session.execute(sql, {"vacc":vacc, "place":place, "date":date})
    db.session.commit()
    return True
