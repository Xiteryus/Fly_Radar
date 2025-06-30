from flask import Flask, render_template, redirect, url_for

#import file 
from flight_radar import * 

app = Flask(__name__)


@app.route('/')
def home():
    data = plane()
    return render_template("index.html", flights=data)



