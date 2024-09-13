def ktsmallestnumber(arr,N,k):
    if len(arr) == 1:
        return arr[0]
    
    arr.sort()
    return arr[k-1]

l = [1,2,4,7,3,5,9,0]

a = ktsmallestnumber(l,8,3)
print(a)

