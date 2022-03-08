import numpy as np
first_array = np.array([1 ,0, 0, 0 ,1, 0])

second_array = np.array([0 ,0, 1, 1 ,0 ,1])


comparison = first_array == second_array

equal_arrays = comparison.all()


print(equal_arrays)