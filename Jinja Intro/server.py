from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    year = datetime.now().year
    return render_template("index.html", year=year)


@app.route("/guess/<name>")
def guesser(name):
    gender_response = requests.get(url=f"https://api.genderize.io?name={name}")
    age_response = requests.get(url=f"https://api.agify.io?name={name}")
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("information.html", name=name.title(), gender=gender, age=age)


@app.route("/blogs")
def blogs():
    blogs_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_blogs = blogs_response.json()
    return render_template("blogs.html", blogs=all_blogs)


if __name__ == "__main__":
    app.run(debug=True)