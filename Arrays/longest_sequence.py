## Brute Force

# def search(arr,num)->bool:
#     n = len(arr)
#     for i in range(n):
#         if (arr[i] == num):
#             return True
    
#     return False


# def length(arr):
#     n = len(arr)
#     length = 0
#     for i in range(n):
#         cnt = 0
#         x = arr[i]

#         while search(arr,x):
#             x += 1
#             cnt +=1
        
#         length = max(length,cnt)
#     return length


## Optimal Approach


def length(arr):
    n = len(arr)
    if n == 0 :
        return 0
    longest = 0 
    st = set()

    for i in range(n):
        st.add(arr[i])
    
    for it in st:
        if it - 1 not in st :
            cnt = 1 
            x = it
            
        while x+1 in st:
            x += 1
            cnt +=1
        longest = max(longest,cnt)
    return longest
        



arr = [100,4,200,1,3,2]

print(length(arr))



