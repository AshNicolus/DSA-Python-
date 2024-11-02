def leader(arr):
    ans = []
    n = len(arr)
    for i in range(n):
        leader = True

        for j in range(i+1,n):
            if (arr[j]>arr[i]):
                leader = False
                break
    
        if leader:
            ans.append(arr[i])
    return  ans


arr = [10, 22, 12, 3, 0, 6]

print(leader(arr))


def printleaders(arr):
    ans = []
    n = len(arr)

    max_elements = arr[n-1]
    ans.append(arr[n-1])
    for i in range(n-2,-1,-1):
        if (arr[i]>max_elements):
            ans.append(arr[i])
            max_elements = arr[i]
    return ans[::-1]


arr = [16,17,4,3,5,2]
print(printleaders(arr))