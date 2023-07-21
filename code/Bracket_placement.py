# bracket placement

def bracket_placement(arr):
    n = len(arr)
    OPTx = [[0] * n for _ in range(n)]  #OPT max
    OPTm = [[0] * n for _ in range(n)]  #OPT min
    path = [[0] * n for _ in range(n)]
    for i in range(1, n - 1):
        path[i][i + 1] = i

    OPTm[0][0] = OPTx[0][0] = abs(arr[0])
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            OPTm[i + 1][i + 1] = OPTx[i + 1][i + 1] = abs(arr[i + 1])
            j = i + length - 1
            cur_max = [OPTx[i][k] + (OPTx[k + 1][j] if sign(arr[k + 1]) == 1 else - OPTm[k + 1][j]) for k in range(i, j)]
            cur_min = [OPTm[i][k] + (OPTm[k + 1][j] if sign(arr[k + 1]) == 1 else - OPTx[k + 1][j]) for k in range(i, j)]
            OPTx[i][j] = max(cur_max)
            OPTm[i][j] = min(cur_min)
            path[i][j] += cur_max.index(max(cur_max))
            if OPTx[i + 1][j] == OPTx[i][j]:
                path[i][j] += cur_max.index(max(cur_max))

    print("OPT max", "\t\t", "OPT min")
    for i in range(n):
        print(OPTx[i], "\t", OPTm[i])
    print()
    for i in range(n):
        print(path[i])
    print(f"Bracket placement for maximum result: {print_matrix(path, arr, 0, n - 1)} = {OPTx[0][n - 1]}")


def sign(num):
    return num // abs(num)


def print_matrix(matrix, arr, i, j):
    if i >= j:
        return str(abs(arr[i]))

    k = matrix[i][j]
    left = print_matrix(matrix, arr, i, k)
    right = print_matrix(matrix, arr, k + 1, j)
    indication = "-" if sign(arr[k + 1]) == -1 else "+"
    return f"({left} {indication} {right})"


numbers1 = [3, -2, -4, 1]   #    (3 - (2 - (4 + 1))) = 6
numbers2 = [3, 4, -2, 5]    #   (3 + ((4 - 2) + 5)) = 10
bracket_placement(numbers1)
print()
bracket_placement(numbers2)
