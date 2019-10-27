"""
Determining a Vector's span

From the lesson on linear combination, recall that the set of all possible vectors that you can reach with a linear
combination of a given pair of vectors is called the span of those two vectors. Let's say we are given the pair of
vectors 𝑣⃗ and 𝑤⃗ , and we want to determine if a third vector 𝑡⃗  is within their span. If vector 𝑡⃗  is
determined to be within their span, this means that 𝑡⃗  can be written as a linear combination of the pair of
vectors 𝑣⃗  and 𝑤⃗ This could be written as:

𝑎𝑣⃗ +𝑏𝑤⃗ =𝑡⃗
,where 𝑣⃗  and 𝑤⃗  are multiplied by scalars 𝑎 and 𝑏 and then added together to produce vector 𝑡⃗ .

"""

"""
Determining Span Computationally

Instead of solving the problem by hand, we are going to solve this problem computationally using NumPy's linear 
algebra subpackage (linalg) . 

Steps to Determine a Vector's Span Computationally:

1. Make the NumPy Python package available using the import method

2.Create right and left sides of the augmented matrix
    2.1 Create a NumPy vector 𝑡⃗ to represent the right side of the augmented matrix.
    2.2 Create a NumPy matrix named 𝑣𝑤 that represents the left side of the augmented matrix (𝑣⃗  and 𝑤⃗)
         
3. Use NumPy's linalg.solve function to check a vector's span computationally by solving for the scalars that make 
the equation true. For this lab you will be using the check_vector_span function you will defined below. 
"""

# Makes Python package NumPy available using import method
import numpy as np

# Creates matrix t (right side of the augmented matrix).
t = np.array([4, 11])

# Creates matrix vw (left side of the augmented matrix).
vw = np.array([[1, 2], [3, 5]])

# Prints vw and t
print("\nMatrix vw:", vw, "\nVector t:", t, sep="\n")

"""
Check Vector's Span with linalg.solve function

You will be using NumPy's linalg.solve function to check if vector 𝑡⃗ is within the span of the other two vectors, 
𝑣⃗  and 𝑤⃗ . To complete this task, you will be inserting your code into the function check_vector_span that is 
defined in the coding cell below. 
"""


def check_vector_span(set_of_vectors, vector_to_check):
    # Creates an empty vector of correct size
    vector_of_scalars = np.asarray([None] * set_of_vectors.shape[0])

    # Solves for the scalars that make the equation true if vector is within the span
    try:
        # TODO: Use np.linalg.solve() function here to solve for vector_of_scalars
        vector_of_scalars = None
        if not (vector_of_scalars is None):
            print("\nVector is within span.\nScalars in s:", vector_of_scalars)
    # Handles the cases when the vector is NOT within the span
    except Exception as exception_type:
        if str(exception_type) == "Singular matrix":
            print("\nNo single solution\nVector is NOT within span")
        else:
            print("\nUnexpected Exception Error:", exception_type)
    return vector_of_scalars


# Call to check_vector_span to check vectors in Equation 1
print("\nEquation 1:\n Matrix vw:", vw, "\nVector t:", t, sep="\n")
s = check_vector_span(vw, t)

# Call to check a new set of vectors vw2 and t2
vw2 = np.array([[1, 2], [2, 4]])
t2 = np.array([6, 12])
print("\nNew Vectors:\n Matrix vw2:", vw2, "\nVector t2:", t2, sep="\n")
# Call to check_vector_span
s2 = check_vector_span(vw2, t2)

# Call to check a new set of vectors vw3 and t3
vw3 = np.array([[1, 2], [1, 2]])
t3 = np.array([6, 10])
print("\nNew Vectors:\n Matrix vw3:", vw3, "\nVector t3:", t3, sep="\n")
# Call to check_vector_span
s3 = check_vector_span(vw3, t3)
