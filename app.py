import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle

app = Flask(__name__)
data_model = pickle.load(open('data_model', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = data_model.predict(final_features)

    output = round(prediction[0], 2)

    if output == 0:
        verdict = 'Le client se desabonne'
    else:
        verdict ='Le client reste abonne'

    return render_template('index.html', prediction_text='Le resultat du client est {}, {}'.format(output,verdict))


if __name__ == "__main__":
    app.run(debug=True)