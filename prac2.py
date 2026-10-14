import numpy as np
#1d array 
a = np.array([1, 2, 4, 5, 7, 6])
print("1D array", a)
#2D array 
b = np.array([[5, 7, 9] ,[2, 1, 11]])
print("2D array", b)
#arange 
c = np.arange(1, 7)
print("Arange:", c)
#Slicing 
print("slicing:", a[1:4])
#Reshaping 
print("Reshaping:", np.reshape(c, (2, 3)))
#mathematical function 
print("Sum:",np.sum(b))
print("Mean:", np.mean(b))
