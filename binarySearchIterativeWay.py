def bsearch(arr,x):
    low =0
    high =  len(arr)-1
    while(low<=high):
        mid = (low+high)//2
        if x == arr[mid]:
            return mid
        elif x> arr[mid]:
            low = mid+1
        elif x < arr[mid]:
            high = mid -1
    return -1


