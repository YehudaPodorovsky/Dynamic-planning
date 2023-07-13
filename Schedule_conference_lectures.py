# Schedule conference lectures
def schedule_conference_lectures(durations, T):
    n = len(durations)
    OPT = [[0] * (T+1) for _ in range(n+1)]

    for i in range(n+1):
        OPT[i][0] = 0
    for j in range(T+1):
        OPT[0][j] = 0

    for i in range(1, n+1):
        for j in range(1, T+1):
            if durations[i-1] <= j:
                OPT[i][j] = max(OPT[i-1][j-durations[i-1]] + 1, OPT[i-1][j])
            else:
                OPT[i][j] = OPT[i-1][j]
    for h in range(len(OPT)):
        print(OPT[h])
    return OPT[n][T]

lectures = [3, 4, 2, 6, 1, 2]
T = 9
print(schedule_conference_lectures(lectures, T))
