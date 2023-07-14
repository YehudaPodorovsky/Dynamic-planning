# segments to schedule
import copy

def schedule_segments(segments):
    n = len(segments)
    segments = sorted(segments, key=lambda x: x[1]) # sort by end time

    # s = Start Time, f = Finish Time
    # To mark each section with whom it does not overlap. complications n^2
    OPT = copy.deepcopy(segments)
    for i in range(n - 1, -1, -1):
        OPT[i].append(-1)
        s = OPT[i][0]
        for j in range(i - 1, -1, -1):
            f = OPT[j][1]
            if s > f:
                OPT[i][2] = j
                break

    # Find the schedule. complications n
    schedule = []
    last_end_time = -1
    for segment in segments:
        start_time, end_time = segment
        if start_time >= last_end_time:
            schedule.append(segment)
            last_end_time = end_time


    for i in range(n):
        print(OPT[i])
    print(schedule)


segments = [
    [9, 12],
    [1, 6],
    [5, 8],
    [1, 9],
    [0, 4],
    [9, 11]
]

schedule_segments(segments)

