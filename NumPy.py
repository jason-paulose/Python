#creating ndarrays
import numpy as np

data = [1,2,3,4,5]
arr1 = np.array(data)
print(arr1)

#creating multidimensional arrays
data2 = [[1,2],[3,4]]
arr2 = np.array(data2)
print(arr2)

#check the dimension of an array
print(arr2.ndim)
print(arr2.shape)

#check the data type of the array
print(arr2.dtype)

#initialize arrays
print(np.zeros(10))
print(np.zeros_like(data2))
print(np.ones(10))
print(np.ones_like(data2))

#cast arrays to different dtypes
float_arr1 = arr1.astype(np.float64)
print(float_arr1.dtype)

strList = ['1','3','5']
npStrArray = np.array(strList)
numArray = npStrArray.astype(np.int64)
print(numArray.dtype)

#operations between arrays
arr = np.array([[1,2,3], [4,5,6]])
arrMultiplied = arr*arr
print(arrMultiplied)
arrSubtracted = arr-arr
print(arrSubtracted)

#operations between arrays and scalars
divideArray = 1/arr
print(divideArray)

#basic indexing and slicing
arr = np.array([0,1,2,3,4,5])
print(arr[1])
print(arr[1:3])
arr[1:3] = 100
print(arr)

# numpy does not copy data, but references the original array
arr = np.array([0,1,2,3,4,5])
arrSlice = arr[1:4]
arrSlice[:] = 10
print(arrSlice)
print(arr)