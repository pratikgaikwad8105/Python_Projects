from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("form.html")


@app.route("/link", methods=["POST"])
def get_data():
    return (f"<h1>Name : {request.form['Name']}\n"
            f"Email : {request.form['email']}</h1>")


if __name__ == "__main__":
    app.run(debug=True)
