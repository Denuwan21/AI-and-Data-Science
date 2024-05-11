import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import pickle
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


df_1.drop(['date', 'street', 'city', 'statezip', 'country'], axis = 1, inplace = True)

df_1.dropna()

df_1['price'] = df_1['price'].astype('int')
df_1['bedrooms'] = df_1['bedrooms'].astype('int')
df_1['bathrooms'] = df_1['bathrooms'].astype('int')
df_1['floors'] = df_1['floors'].astype('int')

X = df_1.drop(['price'], axis = 1)

Y = df_1.price

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2)
x_tr1, x_ts1, y_tr1, y_ts1 = train_test_split(x_test, y_test, test_size = 0.5)

model = LinearRegression()
model.fit(x_train, y_train)

model.score(x_test, y_test)

model.predict([[4, 1, 340, 7912, 1, 0, 0, 3, 1340, 0, 1955, 2005]])

pickle.dump(model,open('model.pkl', 'wb'))

Result = pickle.load(open('model.pkl', 'rb'))