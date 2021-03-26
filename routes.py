from app import app
from flask import render_template, request, redirect
import messages, users

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new")
def new():
    list_users = messages.get_users()
    list_places = messages.get_places() 
    return render_template("new.html", count=len(list_users), list_users=list_users, list_places=list_places)

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
    if messages.send(name,place,vacc,date):
        return redirect("/")
    else:
        return render_template("error.html",message="Viestin lähetys ei onnistunut")

@app.route("/login", methods=["get","post"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["get","post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Rekisteröinti ei onnistunut")
