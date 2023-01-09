def binarySearch(arr, l, r, target):
    m = (l + r)//2
    if(l > r):
        return -1
    if(arr[m] == target):
        return m
    elif(arr[m] > target):
        return binarySearch(arr, l, m-1, target)
    else:
        return binarySearch(arr, m+1, r, target)