# Tracks in Harig

def tracks_in_Harig(arr):
    n = len(arr)

    # reset OPT
    OPT = [[0] * (n + 1) for _ in range(n + 1)]
    maxValue = max([j for i in arr for j in i]) * n
    for i in range(1, n + 1):
        OPT[i][0] = maxValue
        OPT[0][i] = maxValue

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            OPT[i][j] = arr[i - 1][j - 1] + min(OPT[i - 1][j - 1], OPT[i - 1][j], OPT[i][j - 1])

    prev = [[0] * (n + 1) for _ in range(n + 1)]
    i = j = n
    while i * j > 0:
        prev[i][j] = arr[i - 1][j - 1]
        if OPT[i - 1][j - 1] < min(OPT[i - 1][j], OPT[i][j - 1]):
            i -= 1
            j -= 1
        elif OPT[i - 1][j] < min(OPT[i - 1][j - 1], OPT[i][j - 1]):
            i -= 1
        else:
            j -= 1

    path = [x for x in [j for i in prev for j in i] if x != 0]

    print("OPT table")
    for i in range(n + 1):
        print(OPT[i])

    print()
    print("Prev table")
    for i in range(n + 1):
        print(prev[i])

    print()
    print("Path is", path)



c = [
    [3, 5, 0, 8],
    [0, 3, 7, 1],
    [4, 6, 2, 6],
    [6, 1, 9, 1]
]
tracks_in_Harig(c)
