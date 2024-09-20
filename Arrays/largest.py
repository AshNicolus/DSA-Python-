
from typing import List

def largest( arr : List[int]) -> int:
        
    maxi = 0 
    for i in range(len(arr)):
        if arr[i]>maxi:
            maxi = arr[i]
        
    return maxi
    

arr = [2,4,6,2]

print(largest(arr))
