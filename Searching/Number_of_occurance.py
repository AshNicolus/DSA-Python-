# # Brute Force
# def count(arr,x):
#     n = len(arr)
#     cnt = 0 
#     for i in range(n):
#         if (arr[i] == x ):
#             cnt +=1
#     return cnt


# array = [2, 2 , 3 , 3 , 3 , 3 , 4]
# print(count(array,3))


# # Optimal Solution


def firstoccurance(arr,k):
    n = len(arr)
    low = 0 
    high = n -1 
    first = -1
    while low <= high:
        mid = (high+low)//2
        if (arr[mid] == k):
            first = mid 
            high = mid - 1
        elif (arr[mid] < k):
            low = mid + 1
        else:
            high = mid - 1
    
    return first

def lastoccurance(arr,k):
    n = len(arr)
    low = 0
    high = n-1
    last = -1 
    while low<=high:
        mid = (high+low)//2

        if(arr[mid] == k):
            last = mid 

            low = mid + 1
        elif(arr[mid]<k):
            low = mid +1 

        else:
            high = mid - 1
    return last

def firstandlastoccurance(arr,k):
    n = len(arr)
    first = firstoccurance(arr,k)
    if first == -1:
        return -1
    last = lastoccurance(arr,k)
    return (first,last)


def count(arr,k):
    n = len(arr)
    first,last = firstandlastoccurance(arr,k)
    if first == -1:
        return -1
    return last - first + 1

array = [2, 2 , 3 , 3 , 3 , 3 , 4]
print(count(array,3))