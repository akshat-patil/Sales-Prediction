from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
from datetime import datetime

app = Flask(__name__)

# Load the models
model_quantity = joblib.load('sales_quantity_model.pkl')
model_revenue = joblib.load('sales_revenue_model.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form input values
    date = request.form['date']
    region = request.form['region']
    product_name = request.form['product_name']
    quantity_sold = request.form['quantity_sold']
    revenue = request.form['revenue']

    try:
        # Convert date and extract date features
        date_obj = pd.to_datetime(date)
        year = date_obj.year
        month = date_obj.month
        day = date_obj.day

        quantity_sold = float(quantity_sold)
        revenue = float(revenue)

        # Prepare input data for prediction
        input_data = pd.DataFrame({
            'year': [year],
            'month': [month],
            'day': [day],
            'region': [region],
            'product_name': [product_name],
            'quantity_sold': [quantity_sold],
            'revenue': [revenue]
        })

        input_data = pd.get_dummies(input_data, drop_first=True)
        input_data = input_data.reindex(columns=model_quantity.feature_names_in_, fill_value=0)

        # Predict quantity sold and revenue
        prediction_quantity = model_quantity.predict(input_data)
        prediction_revenue = model_revenue.predict(input_data)

        output_quantity = round(prediction_quantity[0])
        output_revenue = round(prediction_revenue[0], 2)

        return render_template('home.html', 
                               prediction_quantity=f"Estimated Quantity Sold: {output_quantity} units", 
                               prediction_revenue=f"Estimated Revenue: ${output_revenue}")
    except Exception as e:
        return render_template('home.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
