def floorandceil(arr,x):
    floor = -1
    ceil = float('inf')
    for num in arr:
        if num <= x:
            floor = max(floor,num)
        if num  >= x:
            ceil = min(ceil,num)
    if ceil == float('inf'):
        ceil = -1 
    return [floor,ceil]


arr = [5, 6, 8, 9, 6, 5, 5, 6]

print(floorandceil(arr,7))