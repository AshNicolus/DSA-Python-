def searc(arr,target):
    low = 0
    n = len(arr)
    high = n -1 
    while low <=high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]<target:
            low = mid +1
        else:
            high = mid - 1
        
    return low


arr= [2,3,5,6,7,8]
print(searc(arr,5))
