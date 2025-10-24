# This file is for the creation of all the vector operations within the calculator
import numpy as np

# these are the vector operators:

# Calculates the magnitude for a vector.
def magnitude(vector):
    vector_magnitude = np.linalg.norm(vector)
    return vector_magnitude


# Function that applies a scalar amount to the vector
def scalar_multiplication(scalar, vector):
    scal_val = scalar * vector
    return scal_val


#Function for dot product of vectors
def dot_product(vector_1, vector_2):
    dot = np.dot(vector_1, vector_2)
    return dot


# Function for cross product of vectors
def cross_product(vector_1, vector_2):
    cross = np.cross(vector_1, vector_2)
    return cross


# Function that finds the theta between two vectors( in rad)
def theta_between_vectorsR(vector_1, vector_2):
    theta = np.arccos( (dot_product(vector_1, vector_2)) /
    ( magnitude(vector_2) * magnitude(vector_1)  ) )
    
    return theta

# Function that finds the theta between two vectors (in deg)
def theta_between_vectors_Deg(vector_1, vector_2):
    theta = np.arccos( (dot_product(vector_1, vector_2)) /
    ( magnitude(vector_2) * magnitude(vector_1)  ) )
    
    return np.rad2deg(theta)


# Function that does addition 
def Resultant_Vector(vector_1, vector_2):
    Resultant = np.add(vector_1, vector_2)
    return Resultant

# Difference function for vectors
def Difference_Vector(vector_1, vector_2):
    Difference = np.subtract(vector_1, vector_2)
    return Difference

