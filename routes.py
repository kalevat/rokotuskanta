from app import app
from flask import render_template, request, redirect
import messages
import users
import random


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/new")
def new():
    list_users = messages.get_users()
    list_places = messages.get_places()
    list_vacc = messages.get_vaccname()
    return render_template("new.html", count=len(list_users), list_users=list_users, list_places=list_places, list_vacc=list_vacc)


@app.route("/search")
def search():
    list_vacc = messages.get_vacc()
    return render_template("search.html", count=len(list_vacc), list_vacc=list_vacc)


@app.route("/send", methods=["post"])
def send():
    name = request.form["name"]
    place = request.form["place"]
    vacc = request.form["vacc"]
    date = request.form["date"]
    vaccname = request.form["vaccname"]
    if messages.send(name, place, vacc, date, vaccname):
        return redirect("/")
    else:
        return render_template("error.html", message="Viestin lähetys ei onnistunut")


@app.route("/login", methods=["get", "post"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")


@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")


@app.route("/register", methods=["get", "post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")


@app.route("/tools", methods=["get", "post"])
def place():
    list_users = messages.get_users()
    if request.method == "GET":
        return render_template("tools.html", list_users=list_users)
    if request.method == "POST":
        place = request.form["place"]
        if messages.update_place(place):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut")


@app.route("/remove", methods=["get", "post"])
def remove():
    if request.method == "GET":
        return render_template("tools.html")
    if request.method == "POST":
        name = request.form["name"]
        messages.remove_name(name)
        return redirect("/")
    else:
        return render_template("error.html", message="Poisto ei onnistunut")


@app.route("/report", methods=["get", "post"])
def report():
    if request.method == "GET":
        list_vacc_users = messages.get_vacc_users()
        list_total_users = messages.get_total_users()
        calc_part = int(list_vacc_users/list_total_users*100)
        list_vacc_total = messages.get_vacc_total()
        vacc_dict = {}
        vacc_names = []
        vacc_total = []
        for t in messages.get_vaccname():
            vacc_dict[t[0]] = 0
        for u in list_vacc_total:
            vacc_dict[u[0]] = u[1]
        for s in messages.get_vaccname():
            vacc_names.append(s[0])
            vacc_total.append(int(vacc_dict[s[0]]/list_vacc_users*100))

        def color():
            color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
            return color
        color_list = [color() for _ in range(0, len(vacc_names))]
        print(color_list)
        return render_template("report.html", calc_part=calc_part, vacc_names=vacc_names, vacc_total=vacc_total, vacc_len=len(vacc_names), color_list=color_list)
