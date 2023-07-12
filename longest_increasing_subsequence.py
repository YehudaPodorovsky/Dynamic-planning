import bisect

def LIS(arr):
    opt = [[arr[i], []] for i in range(len(arr))]
    opt[0][1].append(arr[0])

    for i in range(1, len(opt)):
        opt[i][1] = opt[i - 1][1].copy()
        pile_index = bisect.bisect_left(opt[i][1], opt[i][0]) # Binary search
        if pile_index == len(opt[i][1]):
            opt[i][1].append(opt[i][0])
        else:
            opt[i][1][pile_index] = opt[i][0]

    result = "OPT =\n"
    for i in range(len(opt)):
        result = result + str(opt[i]) + "\n"
    result = result + str(len(opt[i][1]))
    return result

#arr = [3, 1, 4, 1, 5, 9, 2, 6]
arr = [2, 4, 3, 5 ,1, 7 ,6 ,9 , 8]
print(LIS(arr))



