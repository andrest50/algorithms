import time

def multiplyMatricesBruteForce(A, B):
    n = len(A[0])
    C = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = 0
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def multiplyMatricesRecursive(A, B):
    if(type(A) == list):
        n = len(A[0])
        C = [[0 for x in range(n)] for y in range(n)]
    else:
        n = 1
        C = 0
    if(n == 1):
        C = A * B
    else:
        C[0][0] = multiplyMatricesRecursive(A[0][0], B[0][0]) + multiplyMatricesRecursive(A[0][1], B[1][0])
        C[0][1] = multiplyMatricesRecursive(A[0][0], B[0][1]) + multiplyMatricesRecursive(A[0][1], B[1][1])
        C[1][0] = multiplyMatricesRecursive(A[1][0], B[0][0]) + multiplyMatricesRecursive(A[1][1], B[1][0])
        C[1][1] = multiplyMatricesRecursive(A[1][0], B[0][1]) + multiplyMatricesRecursive(A[1][1], B[1][1])
    return C

def main():
    matrix1 = [[2, 3], [4, 5]]
    matrix2 = [[1, 5], [2, -2]]
    matrix3 = [[2, 3, 1], [4, 5, -2], [3, 6, -1]]
    matrix4 = [[1, 5, -3], [2, -2, -4], [2, 1, 5]]
    start = time.time()
    #result = multiplyMatricesRecursive(matrix1, matrix2)
    result = multiplyMatricesBruteForce(matrix3, matrix4)
    end = time.time()
    print("Resultant Matrix: {}".format(result))
    print("Runtime: {:.10f}".format(end - start))

main()