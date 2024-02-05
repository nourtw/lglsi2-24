def multiply_matrices(mat1, mat2):
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]

    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            result[i][j] = sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2)))

    return result

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
result = multiply_matrices(matrix1, matrix2)
print(result)
#initializing 'result' before assigning values to the matrix elements
