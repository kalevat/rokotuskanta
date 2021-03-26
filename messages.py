from db import db
import users

def get_users():
    sql = "SELECT username FROM users"
    result = db.session.execute(sql)
    return result.fetchall()

def get_places():
    sql = "SELECT placename FROM place"
    result = db.session.execute(sql)
    return result.fetchall()


def get_vacc():
    sql = "SELECT u.username, v.vacc, v.date, p.placename FROM vaccination v INNER JOIN place p ON p.id=v.place_id INNER JOIN users u ON u.id=v.user_id"
    result = db.session.execute(sql)
    return result.fetchall()

def send(name,place,vacc,date):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "UPDATE vaccination SET vacc=:vacc, date=:date, place_id=(SELECT id FROM place WHERE placename=:place) WHERE user_id=(SELECT id FROM users WHERE username=:name)"
    db.session.execute(sql, {"vacc":vacc, "place":place, "date":date, "name":name})
    db.session.commit()
    return True
