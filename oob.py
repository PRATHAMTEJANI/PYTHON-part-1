# # class student:
# #     name = "pratham"

# # s1 = student()
# # print(s1.name)    
# # s2 = student()
# # print(s2.name)

# # class car:
# #     color = "blue"

# # car1 = car()
# # print(car1.color)

# class new:
#     def __init__(self, fname , marks , var):  #contsrucor declaration first
#         print("hello pratham tejani..." +fname)
#         self.name = fname
#         self.marks = marks
#         self.var = var

#     def welcome(self):
        
#         print("hello pratham " +str(self.marks))

#     def welcom(self):
        
        
#         print("hello pratham " +str(self.var))

#     def meth1(self):
#         print("help" + self.name)

# s1 = new("pratham" , 32 , 325)
# s1.welcome()
# s1.welcom()
# print(s1.name)
# print(s1.marks)

# s2 = new(" me" , 32 , 65)
# s2.meth1()

# class studemt:
#     def __init__(self, name , marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks :
#             sum = sum + val
#         print("hi" , self.name , "marks" , sum/3)

# s1 = studemt("het" , [50 , 40 , 10])    #for changing use ( . (dot) )
# s1.name = "pratham"
# s1.get_avg()


# class one:
#     @staticmethod
#     def college():
#         print("hellp")

# one.college()         static method in python


# #abstraction :- 
# class car:
#     def __init__(self):
#         self.acc = False        #background
#         self.brk = False        #background
#         self.clut = False       #background

#     def start(self):
#         self.clut = True        #background
#         self.acc = True         #background
#         print("start")

# car1 = car()
# car1.start() 


# #encapsulation :-
# class enca:
#     def __init__(self):
#         self.num = 1
#     def __iter__(self):
#         self.sum = 2

# for  x in range(1,20):
#     print(x)

# def func():
#     x = 300
#     def inner():
#         print(x)
#     inner()
# func()

# x = 5
# print(dir())