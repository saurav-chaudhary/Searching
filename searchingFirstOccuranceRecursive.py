class firstOccur():
    def bsearch(self,arr,low,high,x):
        if low>high:
            return -1
        mid = (low + high)//2
        if x> arr[mid]:
            return self.bsearch(arr,mid+1,high,x)
        elif x < arr[mid]:
            return self.bsearch(arr,low,mid-1,x)
        else:
            if mid ==0 or arr[mid]!=arr[mid-1]:
                return mid
            else:
                return self.bsearch(arr,low,mid-1,x)
arr = [10,20,20,30,35,40]
x = 20
n = len(arr)-1
first = firstOccur()
print(first.bsearch(arr,0,n,x))