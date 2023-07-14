# End of semester

def end_of_semester(tasks):
    n = len(tasks) + 1
    OPT = [[0] * (n) for _ in range(n)]

    for i in range(1, n):
        OPT[i][0] = tasks[i - 1][0] + OPT[i - 1][0]
        for j in range(1, n):
            OPT[i][j] = 0
            for k in range(0, j + 1):
                OPT[i][j] = max(OPT[i][j], OPT[i - 1][k] + tasks[i - 1][j - k])
        print(OPT[i])

tasks = [
    [20, 30, 60, 80],
    [0, 40, 50, 70],
    [15, 20, 40, 90]
]
end_of_semester(tasks)
