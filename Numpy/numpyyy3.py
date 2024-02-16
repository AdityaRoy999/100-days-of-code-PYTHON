#initializing different types of arrays
import numpy as np
import random
#all zeros matrix 
print(np.zeros((2,3)))

#all ones 
print(np.ones((2,2,2)))

#any other number 
print(np.full((2,2),99))

#random decimal numbers,integers
print(np.random.rand(2,4))
print(np.random.randint(2,size=(3,3)))

#identity matrix
print(np.identity(3))

#repeating array n times
arr = np.array([[2,3,4],[4,5,6]])
arr1 = np.repeat(arr,3,axis=0)
print(arr1)


#program 
output = np.ones((5,5))
print(output)
z = np.zeros((3,3))
z[1,1] = 9
print(z)

output[1:4,1:4] = z
print(output)


#be careful while copying araays
a1 = np.array([2,3,4])
b1 = a1
print(b1)


