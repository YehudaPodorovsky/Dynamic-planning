# segments with weight

def segments_with_weight(segments):
    segments.insert(0, [-1, -1, 0])
    n = len(segments)
    segments = schedule_segments(segments) # Sorting and finding an overlapping section

    segments[0].append(segments[0][2])
    for i in range(1, n):
        OPTi = max(segments[i - 1][4], segments[i][2] + segments[segments[i][3]][4])
        segments[i].append(OPTi)
        print(segments[i])

    print()
    print(f"The maximum segment weight sum is {segments[i][4]}")

def schedule_segments(segments):
    n = len(segments)
    segments = sorted(segments, key=lambda x: x[1])

    for i in range(n - 1, -1, -1):
        segments[i].append(-1)
        s = segments[i][0]
        for j in range(i - 1, -1, -1):
            f = segments[j][1]
            if s > f:
                segments[i][3] = j
                break
    return segments

segments = [
    [9, 12, 1],
    [1, 6, 4],
    [5, 8, 4],
    [1, 9, 7],
    [0, 4, 2],
    [9, 11, 2]
]
segments_with_weight(segments)
