#Written by Satwika
import numpy as np
original_vector = np.array([10, 11, 12, 13, 14])
print("Original array:- ")
print(original_vector)
p = 5
new_vector = np.zeros(len(original_vector) + (len(original_vector)-1)*(p))
new_vector[::p+1] = original_vector
print("\n New array:- ")
print(new_vector)