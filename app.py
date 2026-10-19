from flask import Flask, render_template, request, flash, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-secret-before-deployment")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:
            flash("Please fill in every field.", "error")
        elif len(message) > 3000:
            flash("Please keep your message under 3000 characters.", "error")
        else:
            # Demo behavior: do not pretend to send email.
            # Connect a mail provider or database before using this form publicly.
            flash("Thanks! The demo form is working. Add an email service to receive messages.", "success")
        return redirect(url_for("home") + "#contact")

    return render_template("index.html")

if __name__ == "__main__":
    # Local development only. Use a production WSGI server when deploying.
    app.run(debug=True)
