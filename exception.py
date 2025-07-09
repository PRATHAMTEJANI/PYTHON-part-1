# try:
#     print(x)
# # except NameError:
# #     print("x is not declared")
# except:
#     print("an exception occrured")    
# # else:
# #     print("nothing went wrong")
# finally:
#     print("thank you")

# try:
#     f = open("demofile.txt")
#     try:
#         f.write("arjun tejani")
#     except:
#         print("writing time error")
#     finally:
#         f.close()
# except:
#     print("oepning error")

# x = -1
# if x < 0:
#     raise Exception("sorry num. are not to below ")

# x = "hel"
# if not type(x) is int:
#     raise TypeError("only integers are allowed")

# #read F-String function

a = 32
b = 54
c = 3024
myorder = "A = {2} b = {1} and c = {0}"
print(myorder.format(a,b,c))