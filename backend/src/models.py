from sklearn.linear_model import LinearRegression, KNeighborsRegressor, GradientBoostingRegressor, DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split

LinearRegressionModel          = None
KNeighborsRegressorModel       = None
GradientBoostingRegressorModel = None
DecisionTreeRegressorModel     = None

def Means(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    return {'mse' : mse,'mae' : mae}

# Создание и обучение модели линейной регрессии
def LinearRegressionTrain(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=13)

    global LinearRegressionModel
    LinearRegressionModel = LinearRegression()
    LinearRegressionModel.fit(X_train, y_train)

    y_pred = LinearRegressionModel.predict(X_test)
    return {Means(y_test, y_pred)}

def LinearRegressionPredict(X_test):
    y_pred = LinearRegressionModel.predict(X_test)
    return {'y' : y_pred,'x' : X_test}

# Создание и обучение модели K-ближайших соседей
def KNeighborsRegressorTrain(X, y, n_neighbors, weights, algorithm, leaf_size, p):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=13)

    global KNeighborsRegressorModel
    KNeighborsRegressorModel = KNeighborsRegressor(n_neighbors, weights, algorithm, leaf_size, p)
    KNeighborsRegressorModel.fit(X_train, y_train)

    y_pred = KNeighborsRegressorModel.predict(X_test)
    return {Means(y_test, y_pred)}

def KNeighborsRegressorPredict(X_test):
    y_pred = KNeighborsRegressorModel.predict(X_test)
    return {'y' : y_pred,'x' : X_test}

# Создание и обучение модели градиентного бустинга
def GradientBoostingRegressorTrain(X, y, n_estimators=100, learning_rate=0.1, max_depth=3):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=13)

    global GradientBoostingRegressorModel
    GradientBoostingRegressorModel = GradientBoostingRegressor(n_estimators, learning_rate, max_depth)
    GradientBoostingRegressorModel.fit(X_train, y_train)

    y_pred = GradientBoostingRegressorModel.predict(X_test)
    return {Means(y_test, y_pred)}

def GradientBoostingRegressorPredict(X_test):
    y_pred = GradientBoostingRegressorModel.predict(X_test)
    return {'y' : y_pred,'x' : X_test}

# Создание и обучение модели решающего дерева
def DecisionTreeRegressorTrain(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=13)

    global DecisionTreeRegressorModel
    DecisionTreeRegressorModel = DecisionTreeRegressor()
    DecisionTreeRegressorModel.fit(X_train, y_train)

    y_pred = DecisionTreeRegressorModel.predict(X_test)
    return {Means(y_test, y_pred)}

def DecisionTreeRegressorPredict(X_test):
    y_pred = DecisionTreeRegressorModel.predict(X_test)
    return {'y' : y_pred,'x' : X_test}