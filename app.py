#importing required libraries
from flask import Flask, render_template, request # type: ignore
import pickle
import numpy as np # type: ignore

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = pickle.load(open('phishing_model.pkl', 'rb'))

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from form
        features = [
            float(request.form['PrefixSuffix-']),
            float(request.form['SubDomains']),
            float(request.form['HTTPS']),
            float(request.form['AnchorURL']),
            float(request.form['WebsiteTraffic'])
        ]

        # Make prediction
        prediction = model.predict([features])[0]
        result = "Legitimate Website ✅" if prediction == 1 else "Phishing Website ❌"
        
        return render_template('index.html', prediction_text=result)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
