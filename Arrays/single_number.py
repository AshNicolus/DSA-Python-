# #brute force (time limit exceeded)
# def singe(nums):
#     n = len(nums)
#     for i in range(n):
#         arr = nums[i]
#         cnt = 0
#         for j in range(n):
#             if nums[j] == arr:
#                 cnt +=1
#         if cnt == 1:
#             return arr
        



# arr = [2,2,3,3,1]
# print(singe(arr))

# Optimal 

def single(arr):
    n = len(arr)
    hashmap = {}
    for num in arr:
        hashmap[num] = hashmap.get(num,0)+1

    for num,count in hashmap.items():
        if count == 1:
            return num
    return -1


arr = [2,2,3,3,1]
print(single(arr))