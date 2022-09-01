from cmath import sqrt
import pandas as pd
import numpy as np
numbers=[5,30,40,50]
letters=["a","b","c","d"]
scalar=5
dict={"a":10,"b":20}
# pandas_seri=pd.Series(numbers)
# pandas_seri=pd.Series(letters)
# pandas_seri=pd.Series(scalar)
# pandas_seri=pd.Series(5,[0,1,2,3])
pandas_seri=pd.Series(numbers,["a","b","c","d"])
# pandas_seri=pd.Series(dict)
# random_num=np.random.randint(10,100,5)
# pandas_seri=pd.Series(random_num)
# result=pandas_seri[0]
# result=pandas_seri[-1]
# result=pandas_seri[:2]
# result=pandas_seri["a"]
# result=pandas_seri["d"]
# result=pandas_seri[["a","c"]]
# result=pandas_seri.ndim
# result=pandas_seri.dtype
# result=pandas_seri.shape
# result=pandas_seri.sum()
# result=pandas_seri.max()
# result=pandas_seri.min()
# result=np.sqrt(pandas_seri)
# result=pandas_seri>=50
# result=pandas_seri%2==0
# print(pandas_seri[result])

# print(pandas_seri)
# print(result)
opel2018=pd.Series([20,30,40,10],["astra","corsa","mokka","insigna"])
opel2019=pd.Series([40,30,20,10],["astra","corsa","gradland","insigna"])
tolal=opel2018+opel2019
print(tolal["astra"])

