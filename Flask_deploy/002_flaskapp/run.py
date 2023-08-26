from flask import Flask, jsonify, request, render_template
import json
import numpy as np
from joblib import load
import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pylab as plt
import shap
from shap.plots import waterfall


model = load('bank_lgbm_model_best.joblib')
#model = load('bank_xgboost_model_best.joblib')
#X = pd.read_csv('X_test_clean_top80_lgbm-selected_100rows.csv')
X = pd.read_csv('X_test_clean_top80_lgbm-selected.csv')

app = Flask(__name__, static_url_path='/static', template_folder='Templates')

@app.route('/', methods=["GET", "POST"])
def index():
    pred = ""
    conclusion = ""
    pic = ""
    if request.method == "POST":
        index = request.form["index"]
        threshold = request.form["threshold"]
        X1 = X.iloc[[index]] 
        pred = round(model.predict_proba(X1)[0][1], 4)
        if float(pred) > float(threshold):
            conclusion = 'The applicantion of index '+index+ ' shall be rejected, given threshold '+ threshold
        else:
            conclusion = 'The applicantion of index '+index+ ' shall be accepted, given threshold '+ threshold
        pic='1'
        explainer = shap.Explainer(model.predict_proba, X)
        shap_values = explainer(X1)
        plt.clf()
        waterfall(shap_values[0, :, 1], show=False)
        plt.savefig('./static/shap_waterfall1.png', bbox_inches='tight', dpi=200)
    return render_template("index.html", pred=pred, conclusion=conclusion, pic=pic, template_folder='Templates')


if __name__ == "__main__":
    app.run(debug=False, host='127.0.0.1', port=5000)
#if on GCP: app.run(debug=False, host='0.0.0.0', port=5000)

