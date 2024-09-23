def movezeroe(arr):
    move_temp = []
    temp = []
    for i in range(len(arr)):
        if arr[i] != 0:
            move_temp.append(arr[i])
        else:
            temp.append(arr[i])
    arr[:] = move_temp + temp
    return arr

arr = [1,0,2,3,2,0,0,4,5,1]
print(movezeroe(arr))