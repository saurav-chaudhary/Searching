# 1. Nive Approach

# def peakElement(arr,n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 0 if arr[0]>arr[1] else 1
#     else:
#         if arr[0]>arr[1]:
#             return 0
#         if arr[n-1]>arr[n-2]:
#             return n-1
#     for i in range(1,n-1):
#         if arr[i]>arr[i+1] and arr[i]>arr[i-1]:
#             return i
#
# x = [10,20,30,5]
# n = len(x)
# print(peakElement(x,n))

# optimize way
def peakElement(arr,n):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2

        if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == n - 1 or arr[mid] >= arr[mid + 1]):
            return mid
        elif arr[mid] <= arr[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1

    return -1
x = [15,3,19,1,7,11,1,7,7]
n = len(x)
print(peakElement(x,n))


