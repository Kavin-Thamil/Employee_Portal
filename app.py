from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = "secret123"

# DATABASE CONFIG
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employees.db"

db = SQLAlchemy(app)

# DATABASE TABLE
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200))
    uploaded_by = db.Column(db.String(100))

# HOME PAGE
@app.route("/")
def home():
    return render_template("login.html")

# LOGIN
@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    user = Employee.query.filter_by(
        email = email,
        password = password
    ).first()

    if user:
        return redirect("/dashboard")
    
    return "Invalid Login"

# DASHBOARD
@app.route("/dashboard")
def dashboard():
    documents = Document.query.all()

    return render_template(
        "dashboard.html",
        documents = documents
    )

# UPLOAD PAGE
@app.route("/upload-page")
def upload_page():
    return render_template("upload.html")

# HANDLING UPLOAD
@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["document"]
    file.save(os.path.join("uploads", file.filename))

    new_document = Document(
        filename = file.filename,
        uploaded_by = "admin@gmail.com"
    )

    db.session.add(new_document)
    db.session.commit()
    
    flash("File uploaded Successfully")
    return redirect("/dashboard")

if __name__ == "__main__":
    app.run(debug=True)
