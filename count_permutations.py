def count_permutations(n, k):
    OPT = [[0] * (k + 1) for _ in range(n + 1)]
    OPT[0][0] = 1

    for i in range(1, n + 1):
        OPT[i][0] = 1
        for j in range(1, k + 1):
            print(i, j)
            OPT[i][j] = OPT[i - 1][j] + (i - 1) * OPT[i - 1][j - 1]
            for h in range(len(OPT)):
                print(OPT[h])
    return OPT[n][k]

n = 4  # Number of elements
k = 3  # Number of order switches

print(f"The exact number of permutations with {k} order switches for n={n} is: {count_permutations(n, k)}")
