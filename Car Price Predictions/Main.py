from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))



@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/predict', methods = ['POST'])
def predict():
    all_items = [int(x) for x in request.form.values()]
    final_item = [np.array(all_items)]
    prediction = model.predict(final_item)

    output = round(prediction[0], 2)

    return render_template('Home.html', prediction_text = "This Input Prediction is :- ${}".format(output))



@app.route('/predict_api', methods = ['POST'])
def predict_api():
    result = request.get_jason(force = True)
    prediction = model.predict([np.array(list(result.values()))])

    output = prediction[0]
    return jsonify(output)

app.run(debug = True)