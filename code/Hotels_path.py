# hotels path

def hotels_path(hotels, max_days):
    n = len(hotels)

    # Pearson
    pearson = [[x, y, x**2, y**2, x*y] for x, y in hotels]
    x_sum = sum(x[0] for x in pearson)
    y_sum = sum(y[1] for y in pearson)
    xx = sum(xx[2] for xx in pearson)
    yy = sum(yy[3] for yy in pearson)
    xy = sum(xy[4] for xy in pearson)
    x = x_sum / n
    y = y_sum / n
    sx = (xx / n - x**2) ** 0.5
    sy = (yy / n - y**2) ** 0.5
    r = (xy - n * x * y) / ((xx - n * x**2) * (yy - n * y**2)) ** 0.5
    b = r * sy / sx
    a = y - b * x
    print("Pearson table\t", f"y = {round(b, 2)}x {round(a, 2)}")
    for i in range(n):
        print(pearson[i])

    # distances

    d = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1):
            d[j][i] = d[i][j] = ((pearson[i][0] - pearson[j][0]) ** 2 + (pearson[i][1] - pearson[j][1]) ** 2) ** 0.5
    print()
    print("d table")
    for i in range(n):
        print(d[i])

    maxd = round(2 * max([element for row in d for element in row])) # max in d
    OPT = [[maxd] * n for _ in range(n)]

    parent = [[None] * n for _ in range(n)]
    for i in range(2, n):
        for j in range(2, i + 1):
            parent[i][j] = i - 1

    for i in range(1, n):
        OPT[i][1] = d[i][0]
        for j in range(2, i + 1):
            OPT[i][j] = OPT[i - 1][j - 1] + d[i - 1][i]
            for k in range(2, i):
                if OPT[k-1][j-1] + d[i][k-1] < OPT[i][j]:
                    OPT[i][j] = OPT[k - 1][j - 1] + d[i][k - 1]
                    parent[i][j] = k - 1

    print()
    print("OPT table")
    for i in range(n):
        print(OPT[i])
    print()
    print("Parent table")
    for i in range(n):
        print(parent[i])


#           (x, y)
hotels = [(168, 70),
          (174, 72),
          (180, 80),
          (182, 85),
          (187, 80),
          (191, 86)]
max_days = 5
hotels_path(hotels, max_days)

