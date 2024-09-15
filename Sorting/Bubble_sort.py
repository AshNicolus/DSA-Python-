def Bubblesort(arr,n):
    for i in range(len(arr)):
        for j in range(i-1,n-1):
            if (arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
            
    return arr

arr = [4,1,3,9,7]
Bubblesort(arr,5)

print(arr)
