# Maximum consecutive subseries

def maximum_consecutive_subseries(arr):
    n = len(arr)
    OPT = [0] * n
    maxi = 0
    start = 0
    end = 0

    OPT[0] = arr[0]
    for i in range(1, n):
        OPT[i] = max(OPT[i - 1] + arr[i], arr[i])
        if OPT[i - 1] + arr[i] <= arr[i]:
            start = i
        if OPT[i] > maxi:
            maxi = OPT[i]
            end = i

    print("From a series", arr)
    print(f"Maximum consecutive subseries is {arr[start:end + 1]}. sum: {maxi}")

arr = [-1, 4, -3, 5, -1, -1, 1, -1]
maximum_consecutive_subseries(arr)
