## Brute Force
# import math 
# def lowerbound(arr,n,x):
    
#     for i in range(n):
#         if arr[i]>= x :
#             return i
        
#     return n

# arr= [1,2,8,10,11,12,19]
# x = 5 
# math.floor(x)
# print(lowerbound(arr,len(arr),x))
# print(x)

#Using Binary Search 

def findFloor(A,N,X):
    low = 0
    high = N-1
    ans = -1
    while low <= high:
        mid = (high+low)//2
        if A[mid] == X:
            return mid 
        if A[mid] < X:
            ans = mid
            low = mid + 1
        else :
            high = mid - 1
    return ans 


arr= [1,2,8,10,11,12,19]
print(findFloor(arr,len(arr),5))