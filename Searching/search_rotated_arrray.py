def search(arr,k):
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high :
        mid = (low+high)//2
        if (arr[mid] == k):
            return mid
        
        if (arr[low] <= arr[mid]):
            if(arr[low]<=k and arr[mid]>=k):
                high = mid - 1
            else:
                low = mid + 1
            
        else:
            if (arr[mid]<= k and arr[high] >= k):
                low = mid + 1 

            else:
                high = mid - 1
    return -1


