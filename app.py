from flask import Flask,request,render_template,jsonify
from src.GemstonePricePrediction.pipelines.prediction_pipeline import PredictPipeline, CustomData

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")