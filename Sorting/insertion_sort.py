def insert(alist,index,n):
    arr = alist[index]
    j = index - 1
    # Find the correct position for arr in the sorted part of the array
    while(j>=0 and alist[j]>arr):
        alist[j+1] = alist[j]   # Shift elements to the right
        j -=1
    alist[j+1] = arr  # Insert arr at its correct position

def insertionsort(alist,n):
      
    for i in range(n): # Start from index 1, since index 0 is trivially sorted
        insert(alist,i,n)
    return alist

arr = [1,6,2,8,3,10,9]

insertionsort(arr,len(arr))
print(arr)
