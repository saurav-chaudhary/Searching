
def lastOCcur(arr,x):
    low =0
    high = len(arr)-1
    while (low<=high):
        mid =  (low+high)//2
        if x>arr[mid]:
            low = mid +1
        elif x< arr[mid]:
            high = mid -1
        else:
            if mid == len(arr)-1 or arr[mid]!=arr[mid+1]:
                return mid
            else:
                low = mid+1
    return -1

arr = [10,20,20,30,35,40]
x = 20
n = len(arr)-1

print(lastOCcur(arr,x))