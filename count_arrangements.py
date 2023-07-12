def count_arrangements(n):
    OPT = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        OPT[i][1] = 1
        for j in range(2, i + 1):
            OPT[i][j] = OPT[i-1][j] * j + OPT[i - 1][j - 1] * j

    for i in range(n + 1):
        print(OPT[i])
    print("Number of arrangements for", n, "objects:", sum(OPT[i]))


n = 4
count_arrangements(n)
