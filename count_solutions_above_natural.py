def solutions_above_natural(a, b):
    n = len(a)
    b = sum(b)
    OPT = [[0] * (b + 1) for _ in range(n + 1)]

    # Base case: If b is 0, there is one solution (all variables are 0)
    for i in range(n + 1):
        OPT[i][0] = 1

    # Dynamic programming
    for i in range(1, n + 1):
        for j in range(1, b + 1):
            if a[i - 1] <= j:
                OPT[i][j] = OPT[i - 1][j] + OPT[i][j - a[i - 1]]
            else:
                OPT[i][j] = OPT[i - 1][j]

    for h in range(len(OPT)):
        print(OPT[h])
    print("Number of solutions above the natural numbers:", OPT[n][b])

# Example usage
a = [1, 2] # coefficients
b = [6]

solutions_above_natural(a, b)

