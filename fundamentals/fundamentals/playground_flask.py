from flask import Flask, render_template

app = Flask(__name__)

print(__name__)


@app.route("/")

def Welcome():
    return "add '/play/ *a number of your choice* / *a colour of your choice*' to the URL"


@app.route("/play/<number>/<color>")
def play(number, color):
    return render_template("index.html", num=int(number), change=color)


# @app.route("/repeat/<number>/<name>")
# def repeater(name, number):
#     str = ""
#     num = int(number)
#     for i in range(num):
#         str += name
#     return str


if __name__ == "__main__":
    app.run(debug=True)