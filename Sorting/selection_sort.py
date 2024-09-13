def select(arr,i):
    min_index = i 
    for j in range(i+1,len(arr)):
        if (arr[j]<arr[min_index]):
            min_index = j
    return min_index

def selection_sort(arr,n):
    for i in range(n):
        min_index = select(arr,i)

        arr[i],arr[min_index] = arr[min_index],arr[i]

    return arr
        

arr = [5,3,4,2,1]
selection_sort(arr,5)

print(arr)