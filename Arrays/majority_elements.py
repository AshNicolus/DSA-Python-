def majority(arr):
    n = len(arr)
    i = 0
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i] == arr[j]:
                cnt +=1
        
    if cnt > n/2:
        return arr[i]

arr = [3,2,3]
print(majority(arr))            

nums = [2,2,1,1,1,2,2]

print(majority(nums))


# Optimal Solution

def majorityElement(arr):
    n = len(arr)
    if n == 0:
        return None
    count = 0
    candidate = None
    for num in arr :
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1 )
    if arr.count(candidate) > n/2:
        return candidate
    else:
        return -1


            
            