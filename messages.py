from db import db
import users

def get_list():
    sql = "SELECT u.username, v.vacc, v.date, p.placename FROM vaccination v INNER JOIN place p ON p.id=v.place_id INNER JOIN users u ON u.id=v.user_id;"
    result = db.session.execute(sql)
    return result.fetchall()

def send(name,place,vacc,date):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO vaccination (vacc, place_id, date, user_id) VALUES (:vacc, (SELECT id FROM place WHERE placename=:place), :date, (SELECT id FROM users WHERE username=:name))"
    db.session.execute(sql, {"vacc":vacc, "place":place, "date":date, "name":name})
    db.session.commit()
    return True
