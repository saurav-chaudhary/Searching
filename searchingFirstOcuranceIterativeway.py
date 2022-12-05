def bsearch(arr,x):
    low = 0
    high  = len(arr)-1
    while(low<=high):
        mid = (low + high)//2
        if x>arr[mid]:
            low = mid+1
        elif x < arr[mid]:
            high =  mid-1
        else:
            if mid ==0 or arr[mid]!=arr[mid-1]:
                return mid
            else:
                high = mid-1

arr = [10,20,20,30,35,40]
x = 20

print(bsearch(arr,x))

