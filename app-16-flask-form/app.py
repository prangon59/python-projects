from sqlite3 import IntegrityError
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from datetime import datetime
from flask_mail import Mail, Message

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default-secret-key")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USERNAME"] = "twintidebd@gmail.com"
app.config["MAIL_PASSWORD"] = os.getenv("APP_PASSWORD")
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
db = SQLAlchemy(app)

mail = Mail(app)

class Form(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80), unique = True)
    date = db.Column(db.Date)
    occupation = db.Column(db.String(80))


@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        occupation = request.form["occupation"]

        form = Form(first_name=first_name, last_name=last_name,
                    email=email, date=date_obj, occupation=occupation)
        
        try:
            db.session.add(form)
            db.session.commit()
            flash(f"{first_name} Form was submitted successfully", "success")
            message_body = f"Thank you for your submission, {first_name}" \
                            f"Here are your data: \n Name:{first_name} {last_name}\n Email:{email}\n Occupation:{occupation}" \
                            f"Thank you!"
            message = Message(subject="New Form Submission",
                              sender=app.config["MAIL_USERNAME"],
                              recipients=[email],
                              body=message_body)
            mail.send(message)

        except IntegrityError:
            db.session.rollback()
            flash(f"An entry with email {email} already exists.", "danger")
        return redirect(url_for("index"))

    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug = True, port = 5001)