def missing(arr):
    n = len(arr)
    summation = (n *(n+1))//2

    s1 = sum(arr)

    missing_number = summation - s1

    return missing_number


arr = [0,1,2,3,4,5,6,7,9]
print(missing(arr))

#Brute Force 
def missing1(arr):
    n = len(arr)
    for i in range(1,n+1):      
        flag = 0

        for j in range(n):     
            if arr[i] == i:
                flag = i
                break 
            
        if flag == 0:
            return i

arr = [0,1,3]
print(missing1(arr))
