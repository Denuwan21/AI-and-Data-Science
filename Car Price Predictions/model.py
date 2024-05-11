import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import linear_model
import pickle
from sklearn.model_selection import train_test_split

Car = pd.read_csv("toyota.csv")

model = {' GT86':1, ' Corolla':2, ' RAV4':3, ' Yaris':4, ' Auris':5, ' Aygo':6, ' C-HR':7,
       ' Prius':8, ' Avensis':9, ' Verso':10, ' Hilux':11, ' PROACE VERSO':12,
       ' Land Cruiser':13, ' Supra':14, ' Camry':15, ' Verso-S':16, ' IQ':17,
       ' Urban Cruiser':18}

transmission = {'Manual':1, 'Automatic':2, 'Semi-Auto':3, 'Other':4}

fuelType = {'Petrol':1, 'Other':2, 'Hybrid':3, 'Diesel':4}

Car['model'] = Car['model'].map(model)
Car['transmission'] = Car['transmission'].map(transmission)
fuelType['fuelType'] = Car['fuelType'].map(fuelType)

Car["mpg"] = Car["mpg"].astype(int)
Car["engineSize"] = Car["engineSize"].astype(int)

X = Car.drop(["price"], axis = 1)

Y = Car.price

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2)

Final = linear_model.LinearRegression()
Final.fit(x_train, y_train)

Final.score(x_test,y_test)

pickle.dump(Final, open('model.pkl','wb'))

model = pickle.load(open('model.pkl', 'rb'))

