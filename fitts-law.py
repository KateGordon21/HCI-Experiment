# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/informed-consent")
def informed_consent():
    return render_template("informed_consent.html")

@app.route("/experiment")
def experiment():
    return render_template("experiment.html")

app.run(debug=True, port=5000)