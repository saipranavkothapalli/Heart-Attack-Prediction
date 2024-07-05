from flask import Flask, render_template, request
import pickle

app = Flask(__name__, static_url_path='/static')
# load the model
model = pickle.load(open('savemodel.sav', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index1.html', **locals())

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    age = int(request.form['age'])
    sex = int(request.form['sex'])
    cp = int(request.form['cp'])
    trestbps = int(request.form['trestbps'])
    chol = int(request.form['chol'])
    fbs = int(request.form['fbs'])
    restecg = int(request.form['restecg'])
    thalach = int(request.form['thalach'])
    exang = int(request.form['exang'])
    oldpeak = float(request.form['oldpeak'])
    slope = int(request.form['slope'])
    ca = int(request.form['ca'])
    thal = int(request.form['thal'])
    result_val = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])[0]
    if result_val==0:
        result='No risk of Heart Attack!'
    else:
        result='Risk of Heart Attack!'
    return render_template('index1.html', **locals())
