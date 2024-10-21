
# #Brute Force
# def maximum(arr):
#     n = len(arr)
#     maxi = float('-inf')
#     for i in range(n):
#         for j in range(i,n):
#             sum = 0
#             for k in range(i,j+1):
#                 sum += arr[k]
            
#             maxi = max(sum,maxi)
#     return maxi

from typing import List


arr = [1,3,2]


# Optimal Solution

def maximum(arr):
    maxi = float('-inf')
    n = len(arr)
    sum = 0
    for i in range(n):
        sum += arr[i]

        if sum > maxi :
            maxi = sum
        if sum < 0:
            maxi = 0
    return maxi

print(maximum(arr))

# final Approach

def maxSubArray(nums: List[int]) -> int:
        n = len(nums)
        maxi = float('-inf')
        sum = 0
        start = 0
        anstart,endstart = -1,-1
        for i in range(n):

            if sum == 0:
                start = i

            sum += nums[i]

            if sum > maxi :
                maxi = sum
                anstart = start
                endstart = i
            
            if sum < 0:
                sum = 0

        return maxi