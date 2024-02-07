# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
from flask import Flask, render_template, jsonify, request
from datacollection import DataCollector

app = Flask(__name__)
data_collector = DataCollector()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/informed-consent")
def informed_consent():
    return render_template("informed_consent.html")


@app.route("/experiment")
def experiment():
    return render_template("experiment.html")


@app.route('/create_participant', methods=['POST'])
def create_participant():
    participant_number = int(request.form['participant_number'])
    data_collector.create_participant(participant_number)
    return jsonify({'status': 'success'})


@app.route('/initial_click', methods=['POST'])
def initial_click():
    data_collector.initial_click()
    return jsonify({'status': 'success'})


@app.route('/target_click', methods=['POST'])
def target_click():
    error_count = int(request.form['error_count'])
    data_collector.target_click(error_count)
    return jsonify({'status': 'success'})


@app.route('/get_progress', methods=['GET'])
def get_progress():
    progress = data_collector.get_progress()
    return jsonify({'progress': progress})


@app.route('/end_session', methods=['POST'])
def end_session():
    data_collector.end_session()


app.run(debug=True, port=4000)
