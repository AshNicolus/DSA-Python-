#Brute Force
def profit(arr):
    maxpro = 0
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):               #TC --> O(n**2) 
            if (arr[j]>arr[i]):              #SC --> O(1)
                maxpro = max(arr[j]-arr[i],maxpro)
    
    return maxpro


arr = [7,1,5,3,6,4]
print(profit(arr))


