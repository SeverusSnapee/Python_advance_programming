from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Read the housing CSV file
        housing_df = pd.read_csv('housing.csv')
        # Read the loan rates CSV file
        loan_df = pd.read_csv('loan_rates_germany.csv')
    except Exception as e:
        return str(e)

    # Convert DataFrames to list of dictionaries
    housing_data = housing_df.to_dict(orient='records')
    loan_data = loan_df.to_dict(orient='records')

    # Render 'index.html' template with data
    return render_template('index.html', housing_data=housing_data, loan_data=loan_data)

if __name__ == '__main__':
    app.run(debug=True)
