def bsearch(arr,low,high,x):
    if low > high:
        return -1
    mid = (low + high)//2
    if arr[mid] == x:
        return mid
    elif x > arr[mid]:
        return bsearch(arr,mid+1,high,x)
    else:
        return bsearch(arr,low,mid-1,x)

arr = [10,20,30,35,40]
x = 20
n = len(arr)-1
print(bsearch(arr,0,n,x))



