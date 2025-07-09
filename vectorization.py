# import numpy as lp
# arr = lp.array([1 , 2, 3 ,4 ,5])
# result = arr * 2        #vectorization concept
# print(result)

import numpy as ml
def func(x , y):
    return x + y

add = ml.frompyfunc(func , 2 , 1)
print(add([1 , 2, 3, 4] , [5 , 6, 7  , 8 ,]))
print(type(add))        #<class 'numpy.ufunc'>
print(type(ml.concatenate))     #<class 'numpy._ArrayFunctionDispatcher'>
print(type(func))       #class function

if type(ml.add) ==ml.ufunc:
    print("add is ufunc")
else:
    print("add is not ufunc")

#Vectorization is the technique of applying operations directly to entire arrays (or matrices) without explicit loops, using highly
#optimized C code underneath via libraries like NumPy — making your numerical programs efficient, clean, and fast.

print(round(51 / 11 , 3 ))


arr = ml.array([3.14159, 2.71828, 1.41421])
print(ml.around(arr , 3))
print(ml.floor(arr))        ## Round down
print(ml.ceil(arr))         ## Round up
print(ml.trunc(arr))
print(ml.fix(arr))      #print closest to zero

arr = ml.around(3.16666 , 3)
print(arr)

arr =3
print(ml.log10(arr))

arr = ml.random.rand(1,10)
print(arr)
print(ml.log10(arr))

arr = ml.array([3.14159, 2.71828, 1.41421])
print(ml.prod(arr))
