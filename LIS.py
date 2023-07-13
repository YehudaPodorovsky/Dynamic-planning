# LIS
import bisect

def longest_increasing_subsequence(arr):
    OPT = [[arr[i], []] for i in range(len(arr))]
    OPT[0][1].append(arr[0])

    for i in range(1, len(OPT)):
        OPT[i][1] = OPT[i - 1][1].copy()
        pile_index = bisect.bisect_left(OPT[i][1], OPT[i][0]) # Binary search
        if pile_index == len(OPT[i][1]):
            OPT[i][1].append(OPT[i][0])
        else:
            OPT[i][1][pile_index] = OPT[i][0]

    print("OPT table")
    for i in range(len(OPT)):
        print(OPT[i])
    print("longest increasing subsequence is:", len(OPT[i][1]))


arr = [2, 4, 10, 9, 7 ,5, 6, 8 ,3]
longest_increasing_subsequence(arr)



