import numpy as lp
ar1 = lp.array([[1 , 2 , 3] , [4 , 5 , 6]])
ar2 = ([[1 , 2 , 3] , [7 , 8, 9]])
arr3 = lp.concatenate((ar1 , ar2) , axis = 1)
arr3 = lp.hstack((ar1 , ar2))
arr3 = lp.vstack((ar1 , ar2))
arr3 = lp.dstack((ar1 , ar2))
arr3 = lp.array_split(arr3 , 3)
#print(arr1)
print(ar1.shape)

import numpy as mk
arr = mk.array([1 , 2 , 3])
arr = mk.array([1 , 2 , 3] , ndmin= 10)
print(arr)
print(arr , arr.shape)

import numpy as mk
arr = mk.array([1 , 2 , 3 , 4 , 5 , 6])
x = mk.where(arr % 2 == 1)          #order in ODD places    
x = mk.searchsorted(arr , 5 , side='right')        #show index
print(x)

arr1 = mk.array([1 , 2, 3, 4])
arr2 = arr1[[True , True , False , True]]       
#newarray = arr1[arr2]
print(arr2)     #only print true value at same indices

arr1 = mk.array([1 , 2, 3, 4])
arr = arr1 > 2
print(arr)  #filtering array condtion true / false send