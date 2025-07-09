# from numpy import random
# import numpy as mk
# # x = random.randint(1000)
# # x = random.randint(1000 , size = (4, 7))   #row . column
# # x = random.choice([1 , 2 , 3 , 4] , size = (1 , 3))  #choice limited 
# # print(x)

# # x = random.choice([1 , 2 ,3, 4], p = [0.1 , 0.2 , 0.3 , 0.4] , size = (3,6))
# # print(x)

# arr = mk.array([1 , 2, 4 , 5 ,6 , 8 , 9 , 7])
# random.shuffle(arr)     #Shuffle is random and unpredictable each time you run it.
# print(arr)
# print(random.permutation(arr))      #Permutations can be exhaustively listed or chosen randomly from all possible ones.

# import matplotlib.pyplot as pl 
# import seaborn as mk
# mk.displot([[1 , 2, 3 ,4 ] , [4 , 5, 5 , 4 , 5]] , kind = "hist")
# pl.show()

# tips = mk.load_dataset("tips")      #sample data
# mk.scatterplot(x="total_bill" , y = "tip" , data=tips)
# pl.show()

# import matplotlib.pyplot as pl 
# import seaborn as mk
# mk.lmplot([1 , 2, 3, 4 , 5])
# mk.displot([1 , 2, 3, 4 , 5] , bins=6 , kde = True)
# pl.show()

#normal distrubution
from numpy import random
import matplotlib.pyplot as pl
import seaborn as mk
# x = random.normal(size = (9, 9))
# x = random.normal(loc = 5,scale = 7 , size = (2,3))
# print(x)
# mk.displot(random.normal(size = 100) , kind = "hist")
# pl.show()

# loc=50 → mean
# scale=10 → standard deviation
# size=1000 → number of values

# x = random.binomial(n = 10 , p = 0.5 , size = 1000)
# print(x)

# data = {
#     "normal" : random.normal(loc = 50 ,scale = 5 , size = 1000),
#     "binomial" : random.binomial(n =100 , p = 0.5  , size = 1000)
# }
# mk.displot(data , kind = "kde")
# pl.show()

# mk.displot(random.poisson(lam=5 , size=1000))
# pl.show()

# data = {
#     "binomial" : random.binomial(n = 10 , p = 0.5 , size = 1000),
#     "poisson" : random.poisson(lam=10 , size = 1000),
#     "normal" : random.normal(loc = 50 , scale = 5 , size = 1000 )
# }
# mk.displot(data , kind ="kde" )
# pl.show()

#mk.displot(random.uniform(size = (20, 100)) ,kind = "kde")

#mk.displot(random.pareto(a=2, size=1000))
  
x = random.zipf(a=2, size=1000)     #zipf function
mk.displot(x[x<10])

pl.show()