import numpy as np

result=np.array([1,2,3,4,5])
result=np.arange(1,10)
result=np.arange(1,10,2)
result=np.zeros(10)
result=np.ones(10)
result=np.linspace(0,100,5)
result=np.random.randint(0,10)
result=np.random.rand(5)
result=np.random.randn(5)
result=np.arange(50)
np_multi=result.reshape(5,10)
print(np_multi.sum(axis=1))
print(np_multi.sum(axis=0))
result=np.random.randint(0,100,10)
print(result.max())
print(result.min())
print(result.mean())
print(result.argmax())
print(result.argmin())




print(result)



