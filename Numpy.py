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
#[]=rows
#same number or 1 (4,4)
#                 (4,1)
'''
array1 = np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12],
                   [13,14,15,16]]) 

array2 = np.array([[1],[2],[3],[4]]) 

print(array1.shape)
print(array2.shape)
print(array1 * array2)


#multi 1 - 100
array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

print(array1.shape)
print(array2.shape)

print(array1 * array2)
'''


#------------------------------------- functions ------------------------------------------------
'''
#zeros()

array1 = np.zeros(10)
array2 = np.zeros((2,3,10))
print(array2)

#ones()

array1 = np.ones((2,3,10))
print(array1)

#full()

array1 = np.full((2,3,10),9)
print(array1)

#eye()

array1 = np.eye(2,3)
print(array1)

#empty()

array1 = np.empty((2,3))
print(array1)

#arange()

array1 = np.arange(0,100,2) #start, stop, step
print(array1)

#linspace()

array1 = np.linspace(0,10,10) #start, stop, num
print(array1)
'''

#------------------------------------- aggregate functions ------------------------------------------------
'''
array = np.array([[1,2,3,4,5],
                 [6,7,8,9,10]])

print(np.sum(array)) # Sum of all elements
print(np.mean(array)) # Average of all elements
print(np.std(array)) # Measure of spread
print(np.var(array)) # Square of standard deviation
print(np.min(array)) # Smallest value
print(np.max(array)) # Largest value
print(np.argmin(array)) # Position (flattened) of smallest
print(np.argmax(array)) # Position (flattened) of largest

print(np.sum(array, axis=0)) # sum column-wise (vertically)
print(np.sum(array, axis=1)) # sum row-wise (horizontally)

'''
#------------------------------------- Filtering ------------------------------------------------

'''
ages = np.array([[21,17,19,20,16,30,18,65],
                 [39,22,15,99,18,19,20,21]])

teenagers = ages[ages < 18]
# adults = ages[(ages >= 18) & (ages < 65)]
seniors = ages[ages >= 65]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]

adults = np.where(ages>=18,ages,0)


print(adults)
'''
#------------------------------------- Random numbers ------------------------------------------------
#seed = same results(lock)
'''
rng = np.random.default_rng() 

#integers
print(rng.integers(low=1, high=7, size=(3, 4))) # 3x4 array of Ints

#floats
np.random.seed()
print(np.random.uniform(low=-1, high=1, size=(3, 2))) # floats between 2 values

# Shuffle
array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)

# Random Choice
fruits = np.array(["🍎", "🍊", "🍌", "🥥", "🍍"])
print(rng.choice(fruits, size=(3, 3)))
'''


#------------------------------------- Saving and loading NumPy arrays ------------------------------------------------
'''
#saving

array = np.array([[1,2,3],[4,5,6]])

np.save('data',array)

print('numpy array was saved!')

#loading

array = np.load('data.npy')

print(array)

#saving multi arrays

array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([2022, 2023, 2024, 2025])
array3 = np.array([1.1, 2.2, 3.3, 4.4, 5.5])

np.savez("data", array1, array2, array3)

print("NumPy data was saved!")

#Load multiple NumPy arrays

array = np.load("data.npz")
print(array)

print(array["arr_0"])
print(array["arr_1"])
print(array["arr_2"])
'''