import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

train = pd.read_csv('./data/train.csv')
test = pd.read_csv('./data/test.csv')

#Modelo regresión lineal
from sklearn.linear_model import LinearRegression

x_train = np.array(train['GrLivArea']).reshape((-1, 1))
y_train = np.array(train['SalePrice'])

model = LinearRegression(fit_intercept = False)
model.fit(x_train, y_train)

#Se imprimen los parametros de w y b
# print(f"Intercepto (b):  {model.intercept_} ")
# print(f"Pendiente (w):  {model.coef_} ")

# Puntos de la recta
X =  np.linspace(0,train['GrLivArea'].max(), 100 )
Y = model.coef_ * X + model.intercept_

# graficación
train.plot.scatter(x = 'GrLivArea', y = 'SalePrice')
plt.plot(X,Y , '-r')
plt.ylim(0, train['SalePrice'].max()* 1.1)

plt.savefig('regresion_lineal.png')
