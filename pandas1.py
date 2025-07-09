import pandas as mk
# var = mk.read_csv('data.csv')
# print(var.to_string())

data = {
    'name' : ['arjun' , 'pratham' , 'mafia'] ,
    'age' : [10 , 20 , 30]
}
var1 = mk.DataFrame(data)       #make table of takle value
print(var1)

print(mk.__version__)   #2.3.0

a = [1 , 2, 3]
print(mk.Series(a))     #Seires
var2 = mk.Series(a, index = ["x" , "y" , "z"])
print(var2)
print(var2["y"])    #index store
calories = {"d1" : 420 , "d2" : 320 , "day3" : 560 }        #--1
var3 = mk.Series(calories)
print(var3)
print(mk.Series(calories , index = ["d1" , "d2"]))         #--1

var4 = mk.DataFrame(data)
print(var4)
print(var4.loc[0])      #location of row 
print(var4.loc[[0 , 1]])      #location of row 
print(var2.loc["y"])        #merged 
var4 = mk.DataFrame({'A': range(500)})
print(var4)

var5 = mk.read_json('varr.json')
print(var5.to_string())

data1 = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409.1,
    "1":479.0,
    "2":340.0,
    "3":282.4,
    "4":406.0,
    "5":300.5
}
}
var6 = mk.DataFrame(data1)
print(var6)
#   Duration  Pulse  Maxpulse  Calories
# 0        60    110       130     409.1
# 1        60    117       145     479.0
# 2        60    103       135     340.0
# 3        45    109       175     282.4
# 4        45    117       148     406.0
# 5        60    102       127     300.5

