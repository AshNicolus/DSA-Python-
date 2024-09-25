def sum(arr:list[int],k:int):
    n = len(arr)
    i = 0
    j = 0 
    for i in range(n):
        
        for j in range(i+1,n):
            nums = arr[j]

            if arr[i] + nums == k :
                x = [i,j]

                return x
    
    return -1
arr = [2,7,11,15]

print(sum(arr,9))

arr =[3,2,4]
print(sum(arr,6))


nums = [3,3]
print(sum(nums,6))