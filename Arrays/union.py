def union(arr1, arr2, n, m):
    i = 0
    j = 0
    union = []

    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        else:
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1

    while i < n:
        if len(union) == 0 or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    while j < m:
        if len(union) == 0 or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union

arr1 = [1, 2, 3, 4, 6]
arr2 = [1, 2, 3, 4, 5, 6]

print(union(arr1, arr2, len(arr1), len(arr2)))
