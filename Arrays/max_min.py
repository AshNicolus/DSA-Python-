def max_min(A,N):
    if N ==1:
        return A[0]
    
    if A[0]>A[1]:         # Compare first 2 elements of the array      
        maxi = A[0]
        mini = A[1]
    else:
        maxi = A[1]
        mini = A[0]

    for i in range(2,N):          #INITIALIZE the loop to search for max and min value of array 
        if A[i]>maxi:               #agar array of the index maxi se jyada hoga toh value replace ho jayegi and update to the maxi value 
            maxi = A[i]
        elif A[i]<mini:            # agar array of the index mini se kam hoga toh mini ki value updated hojayegi 
            mini = A[i]
    return maxi + mini              #Yaha pe vvalue return denge maxi and mini ki 

# Drivers code
l = [1,2,3,-1,-6,0]
a = len(l)
x = max_min(l,a)
print(x)