def search(arr,num)->bool:
    n = len(arr)
    for i in range(n):
        if (arr[i] == num):
            return True
    
    return False


def length(arr):
    n = len(arr)
    length = 0
    for i in range(n):
        cnt = 0
        x = arr[i]

        while search(arr,x):
            x += 1
            cnt +=1
        
        length = max(length,cnt)
    return length


arr = [100,4,200,1,3,2]

print(length(arr))







