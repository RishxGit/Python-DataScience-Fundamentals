'''
import numpy as np


array = np.array([1,2,3,4])
array = array * 2
print (array)
'''
import numpy as np
#----------------------DATA TYPES---------------------------


# integer (int8, int16, int32, int64)
# float (float16, float32, float64)
# boolean (bool_)
# string (str_, <U#)
# object (object_)

'''
array = np.array([1,2,3,4,5], dtype = np.float16)

print(array)
print(array.dtype)
print(f'{array.nbytes} bytes')
'''

#--------------------------------multidimensional arrays(INDEXING)--------------------------------------
'''
array = np.array([
    [['A', 'B', 'C'], 
     ['D', 'E', 'F'], 
     ['G', 'H', 'I']],
    
    [['J', 'K', 'L'], 
     ['M', 'N', 'O'], 
     ['P', 'Q', 'R']],

     [['S', 'T', 'U'], 
     ['V', 'W', 'X'], 
     ['Y', 'Z', ' ']]
])
#array[layer, rows, columns]

print(array.ndim)
print(array.shape)
print(array[1,0,2] + array[1,1,2] + array[1,0,2])
'''
#------------------------------------- reshape()----------------------------------------------
#(rows,columns)
#(layers,rows,columns)
#array = array.reshape(-1,1)
'''
array = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

array = array.reshape(2,2,3)

print(array.shape)
print(array)
'''
#------------------------------------- slicing----------------------------------------------
# array[rows, columns]
# array[start:stop:step]SSS
'''
array = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])



print(array[2:4,2:4])

'''

#------------------------------------- ARITHMETIC----------------------------------------------
'''
#scalar arithetic

array = np.array([1,2,3])

print(array + 1)
print(array - 2)
print(array * 3)
print(array / 4)
print(array ** 5)


#vectorized math functions


array = np.array([1.05,2.55,3.99])

print(np.sqrt(array))
print(np.round(array))
print(np.floor(array))
print(np.ceil(array))



#element-wise arithmetic


array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)


#comparison operators
scores = np.array([91,55,100,73,82,64])

print(scores == 100)
print(scores > 60)
print(scores < 60)

scores[scores < 60] = 0
print(scores)

'''


#------------------------------------- broadcasting ------------------------------------------------

