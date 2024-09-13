def segregate_elements(arr):
    positive = []
    negative = []
    for i in range(len(arr[i])):
        if arr[i] >= 0:
            positive.append(arr[i])
        else: 
            negative.append(arr[i])

    arr[:] = positive + negative 
    return arr
