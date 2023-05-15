from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def contact():
    return render_template("contact.html")


@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    name = request.form["username"]
    byear = request.form["byear"]
    bmonth = request.form["bmonth"]
    bday = request.form["bday"]
    high = request.form["high"]
    univ = request.form["univ"]
    rounin = int(request.form["rounin"])
    return render_template(
        "contact_complete.html",
        name=name,
        high=high,
        univ=univ,
        byear=byear,
        bmonth=bmonth,
        bday=bday,
        rounin=rounin,
    )
