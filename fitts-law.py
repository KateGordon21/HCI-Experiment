# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
from flask import Flask

app = Flask(__name__)

@app.route("/")
def landing_page():
    return """<img src="https://cdn.discordapp.com/attachments/1019718536836427837/1197656100351262831/20240118_122620.jpg?ex=65bc0f29&is=65a99a29&hm=2799bebd6f096f500df19e47e5aee639bf02f3a7dd9d58c6fffb7373d85ecae1&" alt="the best boy">
    <title>lmao Ethan is dumb</title>"""

app.run(debug=True, port=5000)