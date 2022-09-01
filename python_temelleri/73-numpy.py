import numpy as np

#python_list
py_list=[1,2,3,4,5,6,7,8,9]
#numpy array
np_arr=np.array([1,2,3,4,5,6,7,8,9])

print(type(py_list))
print((type(np_arr)))

py_multi=[[1,2,3],[4,5,6],[7,8,9]]
np_multi=np_arr.reshape(3,3)

print(py_multi)
print(np_multi)