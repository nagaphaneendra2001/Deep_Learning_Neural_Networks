import numpy as np
from numpy import random

#Creating a random vector of size 20 with float values within the range of 1 to 20
random_vector = random.uniform(1,20,size=(20))

#Reshaping the random_vector using reshape() method
new_random_vector = random_vector.reshape(4, 5)

#Assigning '0' value to the maximum elements along the axis-1
new_random_vector[np.arange(4), new_random_vector.argmax(axis=1)] = 0.00

#Printing the final output
print(new_random_vector)
