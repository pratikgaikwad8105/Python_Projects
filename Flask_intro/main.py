from flask import Flask

app = Flask(__name__)


def make_italic(func):
    return f'<em>{func()}</em>'


def underline(func):
    return f"<u>{func()}</u>"


@app.route("/")
def hello():
    return "Hello_world"


@app.route("/world")
@make_italic
@make_bold
@underline
def world():
    return 'World'



if __name__ == "__main__":
    app.run(debug=True)
