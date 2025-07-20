from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return render_template("input.html")
    else:
        username = request.form["name"]
        return render_template("output.html", display = username)

if __name__ == "__main__":
    app.debug = True
    app.run()