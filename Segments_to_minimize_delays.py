# segments to minimize delays

def minimize_delays(segments):
    segments = sorted(segments, key=lambda x: x[1]) # sort by deadline

    for i in range(len(segments)):
        if i == 0:
            segments[i].append(segments[i][0])
        else:
            segments[i].append(segments[i][0] + segments[i - 1][2]) # end time
        segments[i].append(max(0, segments[i][2] - segments[i][1])) # late
        print(segments[i])

    print(f"The minimum delay for this group will be {segments[i][3]}.")



# segments[i][0] is segment length
# segments[i][1] is deadline
segments = [
    [10, 10],
    [1, 2]
]

minimize_delays(segments)

