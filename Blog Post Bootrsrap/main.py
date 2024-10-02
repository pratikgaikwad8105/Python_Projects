from flask import Flask, render_template, request
import requests
response = requests.get("https://api.npoint.io/aed360971ee78d8015eb")
blog_data = response.json()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", blog_data=blog_data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:post_id>")
def post(post_id):
    required_post = None
    for post in blog_data:
        if post["id"] == post_id:
            required_post = post

    return render_template("post.html", post= required_post)


@app.route("/contact", methods=["post"])
def receive_data():
    return "<h1>Successfully Submitted</h1>"

if __name__ == "__main__":
    app.run(debug=True)
