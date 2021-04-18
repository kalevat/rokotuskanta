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


def get_vaccname():
    sql = "SELECT vaccname FROM vaccine"
    result = db.session.execute(sql)
    return result.fetchall()


def get_vacc():
    sql = "SELECT u.username, v.vacc, v.date, p.placename, c.vaccname FROM vaccination v INNER JOIN place p ON p.id=v.place_id INNER JOIN users u ON u.id=v.user_id INNER JOIN vaccine c ON c.id=v.vacc_id"
    result = db.session.execute(sql)
    return result.fetchall()


def send(name, place, vacc, date, vaccname):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "UPDATE vaccination SET vacc=:vacc, date=:date, place_id=(SELECT id FROM place WHERE placename=:place), vacc_id=(SELECT id FROM vaccine WHERE vaccname=:vaccname)  WHERE user_id=(SELECT id FROM users WHERE username=:name)"
    db.session.execute(sql, {"vacc": vacc, "place": place,
                       "date": date, "name": name, "vaccname": vaccname})
    db.session.commit()
    return True


def update_place(place):
    try:
        sql = "INSERT INTO place (placename) VALUES (:place)"
        db.session.execute(sql, {"place": place})
        db.session.commit()
    except:
        return False
    return True


def remove_name(name):
    try:
        sql = "delete from vaccination where user_id = (select id from users where username = :name)"
        db.session.execute(sql, {"name": name})
        sql = "delete from users where username = :name"
        db.session.execute(sql, {"name": name})
        db.session.commit()
    except:
        return False
    return True


def get_vacc_users():
    sql = "select count(vacc) from vaccination;"
    result = db.session.execute(sql)
    return result.fetchall()[0][0]


def get_total_users():
    sql = "select count(id) from users;"
    result = db.session.execute(sql)
    return result.fetchall()[0][0]


def get_vacc_total():
    sql = "select c.vaccname, count(*) from vaccination v, vaccine c where c.id=v.vacc_id group by c.vaccname;"
    result = db.session.execute(sql)
    return result.fetchall()
