from flask import Flask, render_template, request, redirect, make_response
from random import randint

answers = {
    "ds": {"yes": 0, "no": 0, "notsure": 0},
    "ac": {"yes": 0, "no": 0, "notsure": 0},
    "bl": {"yes": 0, "no": 0, "notsure": 0}
}

voted_users = []

app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return "Страница не найдена"


@app.route("/")
@app.route("/index")
def show_questions():
    if "voted" in request.cookies and request.cookies["voted"] in voted_users:
        return render_template("ready.html")
    else:
        return render_template("questions.html")

@app.route("/delete-cookie")
def delete_cookie():
    response = make_response(redirect("/"))
    voted_users.clear()
    response.set_cookie("voted", max_age=0)
    answers.update({
        "ds": {"yes": 0, "no": 0, "notsure": 0},
        "ac": {"yes": 0, "no": 0, "notsure": 0},
        "bl": {"yes": 0, "no": 0, "notsure": 0}
    })


    return response



@app.route("/results", methods=["GET", "POST"])
def process_results():
    if request.method == "GET":
        return render_template("answers.html", answers=answers)
    if request.method == "POST":
        if "ds" in request.form and request.form["ds"] in ("yes", "no", "notsure"):
            answers["ds"][request.form["ds"]] += 1
        if "ac" in request.form and request.form["ac"] in ("yes", "no", "notsure"):
            answers["ac"][request.form["ac"]] += 1
        if "bl" in request.form and request.form["ac"] in ("yes", "no", "notsure"):
            answers["bl"][request.form["bl"]] += 1
        response = make_response(redirect("/results"))
        s = str(randint(1, 1_000_000_000))
        voted_users.append(s)
        response.set_cookie("voted", s)
        return response

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=4321)
