from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db():
    return sqlite3.connect("database.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        role = request.form["role"]
        if role == "donor":
            return redirect("/donor")
        else:
            return redirect("/receiver")
    return render_template("login.html")

@app.route("/donor", methods=["GET", "POST"])
def donor():
    if request.method == "POST":
        data = request.form
        db = get_db()
        db.execute("""
            INSERT INTO food 
            (name, quantity, type, location, expiry, contact, created_at, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data["name"],
            data["quantity"],
            data["type"],
            data["location"],
            data["expiry"],
            data["contact"],
            datetime.now(),
            "Available"
        ))
        db.commit()
        db.close()
        return redirect("/receiver")
    return render_template("donor.html")

@app.route("/receiver")
def receiver():
    db = get_db()
    foods = db.execute("""
        SELECT * FROM food 
        WHERE status='Available' 
        AND expiry > CURRENT_TIMESTAMP
    """).fetchall()
    db.close()
    return render_template("receiver.html", foods=foods)

@app.route("/accept/<int:id>")
def accept(id):
    db = get_db()
    db.execute("UPDATE food SET status='Accepted' WHERE id=?", (id,))
    db.commit()
    db.close()
    return redirect("/receiver")

if __name__ == "__main__":
    app.run(debug=True)
