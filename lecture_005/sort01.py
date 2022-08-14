def sort01(arr):
    itr = 0
    pt = -1
    n = len(arr)

    while itr < n:
        if arr[itr] == 0:
            pt += 1
            arr[pt], arr[itr] = arr[itr], arr[pt]

        itr += 1
