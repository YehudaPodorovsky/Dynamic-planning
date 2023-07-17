# rising series

def rising_series(arr):
    count = 1
    max_count = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            count += 1
        else:
            count = 1
        max_count = max(count, max_count)

    print(max_count)

arr1 = [2, 5, 7, 18, 3, 4, 9, 6, 5, 7, 10, -3, -2, -1, 0, 1, 3, 5, 7]
arr2 = [2, 5, 7, 18, -3, -2, -1, 0, 1, 3, 5, 7, 3, 4, 9, 6, 5, 7, 10]
rising_series(arr2)
