from src import models
import pandas as pd

train_data = pd.read_excel('src/dataset.xlsx')

X_train = train_data[['YearB', 'Square', 'Technical', 'Residual']]
y_train = train_data['Referred']

print('GradientBoostingRegressor')
result = models.GradientBoostingRegressorTrain(X_train, y_train)
print('mse:', result['mse'])
print('mae:', result['mae'])

print('DecisionTreeRegressor')
result = models.DecisionTreeRegressorTrain(X_train, y_train)
print('mse:', result['mse'])
print('mae:', result['mae'])

print('KNeighborsRegressor')
result = models.KNeighborsRegressorTrain(X_train, y_train)
print('mse:', result['mse'])
print('mae:', result['mae'])

print('LinearRegression')
result = models.LinearRegressionTrain(X_train, y_train)
print('mse:', result['mse'])
print('mae:', result['mae'])