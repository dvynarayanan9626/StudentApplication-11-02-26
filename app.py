from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

# --------------------
# 1️⃣ Signup Page
# --------------------
@app.route("/", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        # Email validation
        if "@" in email and "gmail.com" in email:

            # Password validation
            if (len(password) >= 8 and
                re.search(r"[0-9]", password) and
                re.search(r"[A-Z]", password) and
                re.search(r"[^a-zA-Z0-9]", password)):

                return redirect(url_for("marks", username=name))

        return "Invalid Email or Password!"

    return render_template("signup.html")


# --------------------
# 2️⃣ Marks Entry Page
# --------------------
@app.route("/marks", methods=["GET", "POST"])
def marks():
    name = request.args.get("username")

    if request.method == "POST":
        tamil = int(request.form.get("tamil"))
        english = int(request.form.get("english"))
        math = int(request.form.get("math"))
        science = int(request.form.get("science"))
        social = int(request.form.get("social"))

        total = tamil + english + math + science + social
        percent = (total / 500) * 100

        if percent >= 85:
            grade = "A+"
        elif percent >= 65:
            grade = "A"
        elif percent >= 50:
            grade = "B"
        else:
            grade = "Fail"

        return redirect(url_for("result",
                                username=name,
                                total=total,
                                percent=round(percent),
                                grade=grade))

    return render_template("marks.html", name=name)


# --------------------
# 3️⃣ Result Page
# --------------------
@app.route("/result")
def result():
    name = request.args.get("username")
    total = request.args.get("total")
    percent = request.args.get("percent")
    grade = request.args.get("grade")

    return render_template("result.html",
                           name=name,
                           total=total,
                           percent=percent,
                           grade=grade)


if __name__ == "__main__":
    app.run(debug=True)
