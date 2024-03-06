import pandas
from sklearn.linear_model import LinearRegression
data= pandas.read_csv('iphone_price.csv')
model = LinearRegression()
model.fit(data[['version']], data[['price']])
A=int(input('Enter any model number:'))
print(model.predict([[A]]))