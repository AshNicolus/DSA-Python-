def reverse(arr,start,end):
    while start<end:
        arr[start],arr[end] = arr[end],arr[start]
        start +=1
        end -=1
    return arr

def rotate(arr,k):
    k = k%len(arr)
    reverse(arr,0,len(arr)-1)
    reverse(arr,0,k-1)
    reverse(arr,k,len(arr)-1)
    return arr


k =2
arr = [1,2,3,4,5]
print(rotate(arr,k))