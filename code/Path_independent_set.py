# Path independent set

def independent_set(arr):
    n = len(arr)
    OPT = [0] * n

    for i in range(0, n):
        if i < 2:
            OPT[i] = arr[i]
        else:
            OPT[i] = max(OPT[i - 2] + arr[i], OPT[i - 1])
    print(OPT)

arr = [1, 8, 6, 3, 6]
independent_set(arr)
