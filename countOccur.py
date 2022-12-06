def count_occur(arr,x):
    first = firstOccur(arr,x)
    if first  == -1:
        return 0
    else:
        return lastOccur(arr,x)-first +1


def firstOccur(arr,x):
    low = 0
    high = len(arr)-1
    while(low<=high):
        mid = (low+high)//2
        if x> arr[mid]:
            low = mid +1
        elif x< arr[mid]:
            high = mid -1
        else:
            if mid ==0 or arr[mid] != arr[mid-1]:
                return mid
            else:
                high = mid -1
    return -1
def lastOccur(arr,x):
    low = 0
    high = len(arr) - 1
    while (low <= high):
        mid = (low + high) // 2
        if x > arr[mid]:
            low = mid + 1
        elif x < arr[mid]:
            high = mid - 1
        else:
            if mid == len(arr)-1 or arr[mid]!=arr[mid+1]:
                return mid
            else:
                low = mid+1
    return -1

arr = [10,20,20,30,35,40]
x = 20


print(count_occur(arr,x))

