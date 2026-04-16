from flask import Flask, render_template_string
from data_store import load_data
from data.analysis import analyze_trend, predict_temperature
app = Flask(name)
HTML = """
<h2>Weather Dashboard</h2>
<p>Average Temp: {{stats.avg_temp}} °C</p>
<p>Max Temp: {{stats.max_temp}} °C</p>
<p>Min Temp: {{stats.min_temp}} °C</p>
<p>Tomorrow Prediction: {{prediction}} °C</p>
"""
@app.route("/")
def dashboard():
   df = load_data()
   stats = analyze_trend(df)
   prediction = predict_temperature(df)
   return render_template_string(HTML, stats=stats, prediction=prediction)
if name == "main":
   app.run(debug=True)
# from flask import Flask, render_template_string
# from data_store import load_data
# from analysis import analyze_trend, predict_temperature
# app = Flask(name)
# HTML = """
# <h2>Weather Dashboard</h2>
# <p>Average Temp: {{stats.avg_temp}} °C</p>
# <p>Max Temp: {{stats.max_temp}} °C</p>
# <p>Min Temp: {{stats.min_temp}} °C</p>
# <p>Tomorrow Prediction: {{prediction}} °C</p>
# """
# @app.route("/")
# def dashboard():
#    df = load_data()
#    stats = analyze_trend(df)
#    prediction = predict_temperature(df)
#    return render_template_string(HTML, stats=stats, prediction=prediction)
# if name == "main":
#    app.run(debug=True)