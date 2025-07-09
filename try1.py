# # # def func(name):
# # #     print("hello" +name)

# # # person1 = {
# # #     "name" : "johni" , 
# # #     "age" : 36 , 
# # #     "country" : "norway"
# # # }    

# # import json

# # x = '{"name": "one" , "age": 36 , "city": "bruce"}'
# # #print(age)
# # y=json.loads(x)  #json to python
# # print(y["age"])

# # y = json.dumps(x)  #python to json
# # print(y)
# # # y = json.dump(x)
# # # print(y)

# # x = {
# #   "name": "John",
# #   "age": 30,
# #   "married": True,
# #   "divorced": False,
# #   "children": ("Ann","Billy"),
# #   "pets": None,
# #   "cars": [
# #     {"model": "BMW 230", "mpg": 27.5},
# #     {"model": "Ford Edge", "mpg": 24.1}
# #   ]
# # }

# # z = json.dumps(x)  #json use for storing the all information in single variable
# # print(json.dumps(x, indent=4))
# # print(z)
# # print(json.dumps(x, indent=4,sort_keys=True))

# import re

# x = "the rain is Unstoppable hoy"
# y = re.search("hellp" , x)
# print(y)
# z = re.search("^the.*hoy$" ,x)
# print(z)

# if z:
#     print("matched")
# else:
#     print("not matched")    

# print(re.findall("ain" , x))
# w = re.findall("Portugal", x)   
# print(w)


# Y = "the rain is Unstoppable Hoy"
# e = re.search("\H" , Y)
# print(e.start())
# o = re.split("\H" , Y , 1)
# print(o)

import camelcase  #pip install camelcase run in terminal for add own library


c = camelcase.CamelCase()

txt = "pratham wants to made new library in python"

print(c.hump(txt))

#This method capitalizes the first letter of each word.
