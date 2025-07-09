# # import numpy

# # arr = numpy.array([1, 2, 3, 4, 5])

# # print(arr)

# import numpy as ny
# arr = ny.array([9 , 8 , 7 , 6 , 5])   #1-D array
# print(arr)
# print(type(arr))

# print(ny.__version__)

# ar = ny.array(34)  #0-D array
# print(ar)

# a = ny.array([[ 1 , 2 , 3] , [4 , 5 , 6]])   #2-D array
# print(a)

# print("_______________")

# b = ny.array([[1 , 2 , 3] , [4 , 5 , 6] , [7 , 8 , 9]])
# print(b)

# print(b.ndim)       #for checking dimensional
# print(a.ndim)
# print(ar.ndim)
# print(arr.ndim)

# var = ny.array([1 , 2 , 3 , 4] , ndmin = 4+10)      #[[[[[[[[[[[[[[1 2 3 4]]]]]]]]]]]]]]
# print(var)

# var1 = ny.array([[[1 , 2 , 3] , [4 , 5, 6]] , [[7 , 8 , 9] , [1 ,5 , 9]]])  #3-D dimensional array
# print(var1)
# print(var1.shape)
# print(var1.size)

# arr = ny.array([1, 2, 3, 4, 5, 6, 7 , 8 , 9 , 10])
# print(arr[1:8:2])       #[start : stop : step]
# print(arr[::2])

# print(arr.dtype)        # DATA TYPE
# arr = ny.array(['apple', 'banana', 'cherry'])
# print(arr.dtype)            #U → means Unicode string type {<U6}
# print(arr)

# #arr = np.array([1, 2, 3, 4], dtype='i4') (-2,147,483,648 to +2,147,483,647)


# arr = ny.array([1, 2, 3, 4, 5, 6, 7 , 8 , 9 , 10])
# newarr = arr.astype(bool)
# print(newarr)

# import numpy as lp

# arr = lp.array([1,2,3,4,5])
#x = arr.copy()      #for copyingthe array { changes = F }
# x=arr.view()        #for view only  
# arr[0] = 4
# x[2] = 20           # connected changes = changes
# print(arr)
# print(x)

# print(x.base)   #owns
#The copy returns None.
#The view returns the original array.

import numpy as lp
arr = lp.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    print(x)

for x in arr:
    for y in x:
        for z in y:
            print(z)

for x in lp.nditer(arr):
    print(x)

for idx,x in lp.ndenumerate(arr):     #index of number in bits
    print(idx,x)