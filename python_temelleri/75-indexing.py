from unittest import result
import numpy as np
numberss=np.array([0,10,15,20,25,30,35,40,45,50,55])
result=numberss[5]
result=numberss[-1]
result=numberss[0:3]
result=numberss[::-1]
numberss=np.array([[0,10,15],[20,25,30],[35,40,45]])
result=numberss[0,2]
result=numberss[:,2]
result=numberss[:,0:2]
result=numberss[-1:,0:2]
result=numberss[-1,:]
result=numberss[:2,:2]

arr1=np.arange()    
arr2=arr1.copy()
arr2[0]=20
print(result)
