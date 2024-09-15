# def reversearr(arr):  # This is for loops
#     n = len(arr)
#     for i in range(n//2):
#         arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
#     return arr
#
#
# arr = [1,2,4,5,67,4]
# reversearr(arr)
# print(arr)
#
#
#
def recursion(ar, i):  # This is done by single pointer recusrion
    n = len(ar)
    if i >= n // 2:
        return
    else:
        ar[i], ar[n - i - 1] = ar[n - i - 1], ar[i]
        recursion(ar, i + 1)


arr = [1, 2, 3, 4, 5, 6]
recursion(arr, 0)
print(arr)
