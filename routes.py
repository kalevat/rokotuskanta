from app import app
from flask import render_template, request, redirect
import messages, users, random

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
        return render_template("new.html", message="Viestin lähetys ei onnistunut", error_message=1)

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
            return render_template("login.html", message="Väärä tunnus tai salasana", error_code=1)

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
            return render_template("register.html", message="Rekisteröinti ei onnistunut", error_code=1)

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
            return render_template("tools.html", message="Rekisteröinti ei onnistunut", error_code=1, list_users=list_users)

@app.route("/remove", methods=["get", "post"])
def remove():
    list_users = messages.get_users()
    if request.method == "GET":
        return render_template("tools.html")
    if request.method == "POST":
        name = request.form["name"]
        messages.remove_name(name)
        return redirect("/")
    else:
        return render_template("tools.html", message="Poisto ei onnistunut", error_message=1, list_users=list_users)

@app.route("/rights", methods=["get", "post"])
def rights():
    list_users = messages.get_users()
    if request.method == "GET":
        return render_template("tools.html")
    if request.method == "POST":
        name = request.form["name"]
        user_rights= request.form["rights"]
        messages.change_rights(name, user_rights)
        return redirect("/")
    else:
        return render_template("tools.html", message="Muutos ei onnistunut", error_message=1, list_users=list_users)


@app.route("/report", methods=["get"])
def report():
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
    return render_template("report.html", calc_part=calc_part, vacc_names=vacc_names, vacc_total=vacc_total, vacc_len=len(vacc_names), color_list=color_list)
