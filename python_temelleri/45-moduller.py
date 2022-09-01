# #yöntem 2
# # import math as islem

# # # value= dir(math)
# # # value=help(math)
# # # value=help(math.factorial)
# # # value=math.sqrt(49)
# # value=islem.sqrt(49)
# # print(value)

# from math import *#herşeyi import etmek denir
# value=factorial(5)

import random
# result= dir(random)
# result=help(random)

result= random.random()
result=random.uniform(1,10)
result=random.randint(1,100)
names=["celal","hasan","rambo","hakko"]
result=names[random.randint(0,len(names)-1)]
result=random.choice(names)
result = random.choice("greeting")

liste = list(range(10))
random.shuffle(liste)
result = liste

liste = range(100)
result = random.sample(liste, 3)
result = random.sample(names, 2)

print(result)