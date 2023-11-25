from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import models

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/train', methods=['POST'])
def train():
    if request.is_json:

        input_data = request.json

        if 'csvFile' in request.files:
            uploaded_file = request.files['csvFile']
            if uploaded_file.filename != '':
                train_data = pd.read_excel[uploaded_file]
                if input_data['X_col'] & input_data['Y_col']:
                    X_train = train_data[input_data['X_col']]
                    y_train = train_data[input_data['Y_col']]
                else:
                    return jsonify({'error': 'Invalid X_col & Y_col!'})
            else:
                return jsonify({'error': 'Invalid File Name!'})
        else:
            train_data = pd.read_excel('dataset.xlsx')
            X_train = train_data[['YearB', 'Square', 'Technical', 'Residual']]
            y_train = train_data['Referred']

        if input_data['model_type'] == 1:
            result = models.GradientBoostingRegressorTrain(X_train, y_train)
        elif input_data['model_type'] == 2:
            result = models.DecisionTreeRegressorTrain(X_train, y_train)
        elif input_data['model_type'] == 3:
            result = models.KNeighborsRegressorTrain(X_train, y_train)
        elif input_data['model_type'] == 4:
            result = models.LinearRegressionTrain(X_train, y_train)
        else:
            return jsonify({'error': 'Invalid Model Type!'})
        
        return jsonify({'mse' : result['mse'].tolist(),'mae' : result['mae'].tolist()})
    else:
        return jsonify({'error': 'Invalid JSON Data'}), 400

@app.route('/predict', methods=['POST'])
def predict():
    if request.is_json:

        input_data = request.json

        if input_data['model_type'] == 1:
            result = models.GradientBoostingRegressorPredict(input_data['X_test'])
        elif input_data['model_type'] == 2:
            result = models.DecisionTreeRegressorPredict(input_data['X_test'])
        elif input_data['model_type'] == 3:
            result = models.KNeighborsRegressorPredict(input_data['X_test'])
        elif input_data['model_type'] == 4:
            result = models.LinearRegressionPredict(input_data['X_test'])
        else:
            return jsonify({'error': 'Invalid Model Type!'})
        
        return jsonify({'y': result['y'].tolist(), 'x': result['x'].tolist()})
    else:
        return jsonify({'error': 'Invalid JSON Data'}), 400

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
