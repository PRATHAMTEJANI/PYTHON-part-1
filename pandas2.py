import pandas as mk

var = mk.read_csv('data.csv')
print(var)
print(var.info())
print(var.shape)
print(var.columns)
print(list(var.columns))
print(var.isnull().sum())   # Checks for missing (NaN) values in each column and sums them up.
print(var.dropna())
print(var.fillna(00))
print(var.describe(include='all'))