from unittest import result
import numpy as np
result=np.array([10,15,30,45,60])
result=np.arange(5,15)
result=np.arange(50,100,5)
result=np.zeros(10)
result=np.ones(10)
result=np.linspace(0,100,5)
result=np.random.randint(10,30,5)
result=np.random.randn(10)
matris=np.random.randint(-50,50,15).reshape(3,5)
result=matris.sum(axis=1)
result=matris.sum(axis=0)
result=matris.max()
result=matris.min()
result=matris.mean()
result=matris.argmax()
result=matris.argmin()
arr=np.arange(10,20)
result=arr[:3]
result=arr[::-1]
result=matris[0]
result=matris[2,3]
result=matris[:,0]
result=matris**2
cif=matris[matris%2==0]
poz_cif=cif[cif>=0]

print(poz_cif)
print("-----------------")
print(matris)
print(result)