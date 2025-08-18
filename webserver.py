from flask import Flask, render_template, redirect, url_for
from flight_radar import plane  # importe ta fonction

app = Flask(__name__)

@app.route('/')
def home():
    data = plane()
    return render_template("index.html", flights=data)

if __name__ == "__main__":
    app.run(debug=True)
