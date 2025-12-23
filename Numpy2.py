import numpy as np

print("NUMPY FUNCTIONS PRACTICE - ALL MAJOR FUNCTIONS COVERED")

#Create array
print("\n1. ARRAY CREATION FUNCTIONS:")

# From lists/tuples
arr1 = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"np.array(): {arr1}")
print(f"2D array:\n{arr2d}")

# Special arrays
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
empty = np.empty((2, 2))  # Uninitialized
identity = np.eye(3)
full = np.full((2, 3), 7)  # Fill with 7

# Sequences
range_arr = np.arange(0, 10, 2)  # 0 to 10 step 2
linspace = np.linspace(0, 1, 5)  # 5 points from 0 to 1
logspace = np.logspace(0, 2, 5)  # 5 points log scale

print(range_arr)
print(linspace)
print(logspace)

# Random arrays
random_arr = np.random.rand(3, 3)  # Uniform [0,1]
randint_arr = np.random.randint(1, 100, (3, 3))  # Random integers
normal_arr = np.random.randn(3, 3)  # Normal distribution
choice_arr = np.random.choice([1, 2, 3, 4], size=(2, 3))

print(random_arr)
print(randint_arr)

# Attributes
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr.shape)
print(arr.size)
print(arr.ndim)
print(arr.dtype)
print(arr.itemsize)

#reshape
arr = np.arange(12)
print(arr)

# Reshape
reshaped = arr.copy()
reshaped = arr.reshape(3, 4)
print(reshaped)

# Flatten and Ravel
flattened = reshaped.flatten()    #output: 
raveled = reshaped.ravel()  #output:

# Can do Tranpose, swap, stacked, split

#Indexing & Slicing
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)

# Basic indexing
print(f"arr[1,2]: {arr[1, 2]}")
print(f"arr[0]: {arr[0]}")  # First row
print(f"arr[:,1]: {arr[:, 1]}")  # Second column

# Slicing
print(f"arr[1:3, :]:\n{arr[1:3, :]}")
print(f"arr[:, ::2]:\n{arr[:, ::2]}")  # Every other column
print(f"arr[::-1]:\n{arr[::-1]}")  # Reverse rows

# Boolean indexing
bool_idx = arr > 5
print(f"Boolean mask (arr > 5):\n{bool_idx}")
print(f"arr[arr > 5]: {arr[arr > 5]}")

# Fancy indexing
rows = np.array([0, 2])
cols = np.array([1, 2])
print(f"arr[[0,2], [1,2]]: {arr[rows, cols]}")

#Math fuctions
print(f"np.abs(): {np.abs(arr)}")
print(f"np.floor(): {np.floor(arr)}")
print(f"np.round(1): {np.round(arr, 1)}")
print(f"np.sqrt(): {np.sqrt(np.abs(arr)).round(2)}")
print(f"np.square(): {np.square(arr)}")
print(f"np.power(arr, 3): {np.power(arr, 3)}")

#Satistical
print(f"np.mean(): {np.mean(arr)}")
print(f"\nnp.median(): {np.median(arr)}")
print(f"np.std(): {np.std(arr)}")
print(f"np.var(): {np.var(arr)}")
print(f"np.min(): {np.min(arr)}")
print(f"np.max(): {np.max(arr)}")
print(f"np.percentile(50): {np.percentile(arr, 50)}")
print(f"np.quantile(0.75): {np.quantile(arr, 0.75)}")

#Sort & Search
print("Sorting & Searching in arr:" )
print(f"np.sort(): {np.sort(arr)}")
print(f"np.argsort(): {np.argsort(arr)}")
print(f"np.unique(): {np.unique(arr)}")
print(f"np.where(arr > 3): {np.where(arr > 3)}")

#String operations
print("String operat... in arr:" )
arr = np.array(['hello', 'world', 'numpy', 'practice'])
print(arr)

print(f"np.char.upper(): {np.char.upper(arr)}")
print(f"np.char.capitalize(): {np.char.capitalize(arr)}")
print(f"np.char.replace('l', 'L'): {np.char.replace(arr, 'l', 'L')}")
print(f"np.char.join('-', arr): {np.char.join('-', arr)}")
print(f"np.char.startswith('h'): {np.char.startswith(arr, 'h')}")
print(f"np.char.find('o'): {np.char.find(arr, 'o')}")
