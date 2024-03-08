from numpy import matrix, linalg
from Matrix import rankMatrix
print("1/ Define a function that return the sum of two numbers a and b. Try with a=3, b=4.")
def sum_two_numbers(a, b):
    return a + b
print(f"sum={sum_two_numbers(3,4)}")

print("2/ Create a 3x3 matrix M=[[1,2,3],[4,5,6],[7,8,9]] and vector v=[1,2,3] \nand check the rank and the shape of this matrix and vector v.")
M=[[1,2,3],[4,5,6],[7,8,9]]
M=rankMatrix(M)
def shape(Matrix):
    if type(Matrix[0]) == list:
        return (len(Matrix), len(Matrix[0]))
    else:
        return (len(Matrix), 1)

print(M.rankOfMatrix(M))
# Matrix = matrix(M)
# print(f"rank(M) = {linalg.matrix_rank(Matrix)}, shape(M) = {Matrix.shape}")
# v=[1,2,3]
