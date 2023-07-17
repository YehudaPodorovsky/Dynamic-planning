# Penguin Journey

def penguin_Journey(north, south, d):
    n = len(north)
    OPT = [[0] * (d + 2) for _ in range(n)]

    OPT[0][0] = south[0]
    print("OPT table")
    for i in range(n):
        OPT[i][0] = south[i] + OPT[i - 1][0]
        for j in range(1, i + 1):
            if j % 2 == 0:
                OPT[i][j] = south[i] + max(OPT[i - 1][j], OPT[i - 1][j - 1])
            else:
                OPT[i][j] = north[i] + max(OPT[i - 1][j], OPT[i - 1][j - 1])
        print(OPT[i])

    max_value = 0
    for j in range(0, d + 1, 2):
        max_value = max(max_value, OPT[n - 1][j])

    print()
    print(f"Max value is {max_value} with {d} transitions.")


north = [4, 8, 10, 1, 10, 10, 1, 5]
south = [14, 5, 5, 50, 5, 1, 8, 3]
d = 6
penguin_Journey(north, south, d)
