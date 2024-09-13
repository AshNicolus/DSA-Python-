def union1(arr1,arr2):
    a = set(arr1)
    b = set(arr2)

    c = a.union(b)

    return len(c)

a1 = [1, 2 ,3, 4 ,5]
a2 = [-1,-5,3]

print(union1(a1,a2))

