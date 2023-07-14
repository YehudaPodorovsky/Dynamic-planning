# Box tower

def box_tower(box):
    n = len(box)
    box = sorted(box, key=lambda x: x[0], reverse=True)  # sort by W
    OPT = [[0] * n for _ in range(n + 1)]

    print("Sorted input")
    for i in range(n):
        print(box[i])

    print()
    print("OPT table")
    for i in range(n):
        OPT[i][i] = box[i][2]
        for j in range(i):
            if box[i][1] > box[j][1]:
                OPT[i][j] = OPT[i - 1][j]
            else:
                OPT[i][j] = OPT[i - 1][j] + OPT[i][i]
        print(OPT[i])

    print()
    print(f"The maximum tower height is {max(OPT[i])}")


box = [
    [52, 4, 8],
    [55, 9, 2],
    [49, 13, 5],
    [47, 20, 2],
    [40, 6, 3],
    [21, 30, 6],
    [19, 10, 8],
    [12, 12, 1]
]
box_tower(box)
