x = 5
print(type(x))
x = 3.155
print(type(x))

x  = ["a" , "b" , "c" ,  "d"] #lists
print(x)
x  = ("a" , "b" , "c" ,  "d")  #tuples
print(x)

y= range(6)
print(y)

x = "pratham"
def func():
    print("value " + x)

func()

def func1(a , b):
    result = a + b
    return result   
sum = func1(10 , 20)
print("the sum is " , sum)