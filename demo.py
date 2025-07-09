import sys
print(sys.version)

if 3>1 :
 print("greter is three")

if 3>4 :
 print("greter is three") 

x = 4   #comment for use HASHTAG
y=5
z="arjun"
print(x + y)
print(z)

""""    
this is also comment
pratham tejani"
"""

# for type casting in python
x= str(3.23)
y= int(3.32233)
z= float(43)

print(x)
print(y)
print(z)

#double qutes and single qutes
x = "arjun1"
print(x)
x= 'arjun2'
print(x)

#python is case sensitive laguaje  [ a , A ]

#multiple value

x,y,z = "arjun3" , "arjun4" , "arjun5"
print(x)
print(y)
print(z)

x = y = z = "Arjun6"
print(x)
print(y)
print(z)

#unpack collection

fruits = ["apple" , "orange" , "banana"]
x = y = z = fruits
print(x)
print(y)
print(z)
x , y , z = fruits
print(x)
print(y)
print(z)
x = "Python is awesome"
print(x)

x = 4   
y=5
z="arjun"
print(x,y,z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# get datatype :-

x = str("Hello World")

#display x:
print(x)

#display the data type of x:
print(type(x)) 


#random function in Python
import random

print(random.randrange(1, 10))

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[2])
print(len(a))


for x in "ARJUN pratham" :
 print(x)
 
txt = "pratham tejani is not a codder"
print("chate" not in txt) 
print("codder" in txt)
txt = "prtham tejani is not a codder"
if "pratham" in txt:
  print("Yes, 'free' is present.")