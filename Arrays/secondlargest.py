def secondlargest(arr):
    maxi = 0
    second_maxi = 0
    if (len(arr) < 2):
        return -1

    for i in range(len(arr)):
        if(arr[i]>maxi):
            second_maxi = maxi
            maxi = arr[i]
            



    for i in range(len(arr)):
        if arr[i]<maxi and arr[i]> second_maxi:
            second_maxi = arr[i]

        if second_maxi == 0:
            return -1

        else:
            return second_maxi


arr = [0,2,4,3]

print(secondlargest(arr))
