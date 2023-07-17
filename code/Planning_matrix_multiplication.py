# Planning matrix multiplication

def planning_matrix_multiplication(matrix_size):
    n = len(matrix_size)
    OPT = [[0] * n for _ in range(n)]
    path = [[0] * n for _ in range(n)]

    for i in range(n - 2, -1, -1):
        OPT[i][i + 1] = matrix_size[i][0] * matrix_size[i][1] * matrix_size[i + 1][1]   # reset multiplying pairs
        path[i][i + 1] = i
        for j in range(i + 2, n):
            OPT[i][j] = float('inf')
            for k in range(j - i):
                cur = OPT[i][k] + OPT[i + k + 1][j] + matrix_size[i][0] * matrix_size[k][1] * matrix_size[j][1]
                if cur < OPT[i][j]:
                    OPT[i][j] = cur
                    path[i][j] = k

    print("matrix_size")
    for i in range(n):
        print(matrix_size[i])

    print("\nOPT table")
    for i in range(n):
        print(OPT[i])

    print("\npath")
    for i in range(n):
        print(path[i])

    print()
    print(f"Optimal Order of Multiplication: {print_matrix(path, 0, n - 1)}")
    print("Minimum Cost:", OPT[0][n-1])


def print_matrix(matrix, i, j):
    if i >= j:
        return "A" + str(i)

    k = matrix[i][j]
    left = print_matrix(matrix, i, k)
    right = print_matrix(matrix, k + 1, j)

    return "(" + left + " x " + right + ")"

# index 0 is r
# index 1 is c
matrix_size = [
    [5, 4],
    [4, 6],
    [6, 2],
    [2, 7]
]
planning_matrix_multiplication(matrix_size)
