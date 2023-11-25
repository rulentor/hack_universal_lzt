from sklearn.linear_model import LinearRegression, KNeighborsRegressor, GradientBoostingRegressor, DecisionTreeRegressor

LinearRegressionModel          = None
KNeighborsRegressorModel       = None
GradientBoostingRegressorModel = None
DecisionTreeRegressorModel     = None

# Создание и обучение модели линейной регрессии
def LinearRegressionTrain(X_train, y_train):
    global LinearRegressionModel
    LinearRegressionModel = LinearRegression()
    LinearRegressionModel.fit(X_train, y_train)
    return {}

def LinearRegressionPredict(X_test):
    y_pred = LinearRegressionModel.predict(X_test)
    return {'y' : y_pred,'x' : X_test}

# Создание и обучение модели K-ближайших соседей
def KNeighborsRegressorTrain(X_train, y_train, n_neighbors, weights, algorithm, leaf_size, p):
    global KNeighborsRegressorModel
    KNeighborsRegressorModel = KNeighborsRegressor(n_neighbors, weights, algorithm, leaf_size, p)
    KNeighborsRegressorModel.fit(X_train, y_train)
    return {}

def KNeighborsRegressorPredict(X_test):
    y_pred = KNeighborsRegressorModel.predict(X_test)
    return {'y' : y_pred,'x' : X_test}

# Создание и обучение модели градиентного бустинга
def GradientBoostingRegressorTrain(X_train, y_train, n_estimators=100, learning_rate=0.1, max_depth=3):
    global GradientBoostingRegressorModel
    GradientBoostingRegressorModel = GradientBoostingRegressor(n_estimators, learning_rate, max_depth)
    GradientBoostingRegressorModel.fit(X_train, y_train)
    return {}

def GradientBoostingRegressorPredict(X_test):
    y_pred = GradientBoostingRegressorModel.predict(X_test)
    return {'y' : y_pred,'x' : X_test}

# Создание и обучение модели решающего дерева
def DecisionTreeRegressorTrain(X_train, y_train, test_size):
    global DecisionTreeRegressorModel
    DecisionTreeRegressorModel = DecisionTreeRegressor()
    DecisionTreeRegressorModel.fit(X_train, y_train)
    return {}

def DecisionTreeRegressorPredict(X_test):
    y_pred = DecisionTreeRegressorModel.predict(X_test)
    return {'y' : y_pred,'x' : X_test}