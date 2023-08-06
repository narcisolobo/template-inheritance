from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/about")
def about():
    return render_template("about.html")


@app.get("/services")
def services():
    return render_template("services.html")


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)
