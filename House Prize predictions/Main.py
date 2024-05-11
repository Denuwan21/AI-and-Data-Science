from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('Home.html')

@app.route('/predict', methods = ['POST'])
def  predict():

    items = [int (x) for x in request.form.values()]
    Items_2 = [np.array(items)]

    prediction = model.predict(Items_2)
    output = round(prediction[0], 2)  

    return render_template('Home.html', prediction_text = "The Result of Above Details :- ${}".format(output))

app.run(debug = True)