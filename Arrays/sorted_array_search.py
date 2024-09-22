def searchInSorted(arr, N, K):
        
    for i in range(N):
        if (arr[i] == K):
            return 1
    return -1
            
arr = [1,2,3,4,5,6]
K= 3
print(searchInSorted(arr,len(arr),K))