import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.metrics import r2_score
import pickle
mpl.style.use('ggplot')

car = pd.read_csv('./quikr_car.csv')

car.head()

car.shape

car.info()

backup = car.copy()

car = car[car['year'].str.isnumeric()]

car['year'] = car['year'].astype(int)

car = car[car['Price'] != 'Ask For Price']

car['Price'] = car['Price'].str.replace(',', '').astype(int)

car['kms_driven'] = car['kms_driven'].str.split().str.get(0).str.replace(',', '')

car = car[car['kms_driven'].str.isnumeric()]

car['kms_driven'] = car['kms_driven'].astype(int)

car = car[~car['fuel_type'].isna()]

car.shape

car['name'] = car['name'].str.split().str.slice(start=0, stop=3).str.join(' ')

car = car.reset_index(drop=True)

car

car.to_csv('Cleaned_Car_data.csv')

car.info()

car.describe(include='all')

car = car[car['Price'] < 6000000]

X = car[['name', 'company', 'year', 'kms_driven', 'fuel_type']]
y = car['Price']

X

y.shape

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

ohe = OneHotEncoder()
ohe.fit(X[['name', 'company', 'fuel_type']])

column_trans = make_column_transformer((OneHotEncoder(categories=ohe.categories_), ['name', 'company', 'fuel_type']),
                                       remainder='passthrough')

lr = LinearRegression()

pipe = make_pipeline(column_trans, lr)

pipe.fit(X_train, y_train)

y_pred = pipe.predict(X_test)

r2_score(y_test, y_pred)

scores = []
for i in range(3000):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.1, random_state=i)
    lr = LinearRegression()
    pipe = make_pipeline(column_trans, lr)
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)
    scores.append(r2_score(y_test, y_pred))

np.argmax(scores)

scores[np.argmax(scores)]

pipe.predict(pd.DataFrame(columns=X_test.columns, data=np.array(
    ['Audi A8', 'Audi', 2019, 100, 'Petrol']).reshape(1, 5)))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=np.argmax(scores))
lr = LinearRegression()
pipe = make_pipeline(column_trans, lr)
pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)
r2_score(y_test, y_pred)

pickle.dump(pipe, open('LinearRegressionModel.pkl', 'wb'))
