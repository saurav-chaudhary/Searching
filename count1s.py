def countOnes( arr, N):
    # Your code here

    if 1 not in arr:
        return 0
    arr.sort()
    print(fistOccur(arr, 1))
    return (N-1) - fistOccur(arr, 1) + 1


def fistOccur( arr, x):
    low = 0
    high = len(arr) - 1
    while (low <= high):
        mid = (low + high) // 2
        if x>arr[mid] :
            low = mid + 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            if mid == 0 or arr[mid - 1] != arr[mid]:
                return mid
            else:
                high = mid - 1
    return -1

arr = [1,1,1,0,0,0,0,0]
n = len(arr)
print(countOnes(arr,n))