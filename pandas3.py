import pandas as mk
import matplotlib.pyplot as pl
var = mk.read_csv('dat.csv')
# # #dev = var.dropna()
# # var.dropna(inplace = True)
# # print(var.to_string())      #row 18 , 22 , 28 removed  beacuse it have null vallue

# # print(mk.read_csv('dat.csv'))

# var.fillna(130000,inplace=True)
# print(var.to_string())      #fill Nan values
# print(var.fillna({"calories":88000} , inplace =True))       #only work in calories Nan value 

# x = var["Calories"].mean()
# x = var["Calories"].median()
# x = var["Calories"].mode()
# x = var["Calories"].mean()
# print(x)

# print(var.to_string())
# print(var.duplicated())

print(var.corr())                       
var.plot()
pl.show()