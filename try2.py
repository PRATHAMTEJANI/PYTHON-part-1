from try1 import person1
print(person1["age"])

import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))  #show days name
x = datetime.datetime(2005 , 11 , 27)
print(x)
print(x.strftime("%B"))  # show month name
print(x.strftime("%V"))  

x = min(5 , 10 , 25)
y = max(10 , 20 , 22)
print(x)
print(y)
x = abs(-3.12) #absolute positive value showing
print(x)
x = pow(3 , 4)
print(x)

import math
x = math.sqrt(81)
x=math.pi
print(x)