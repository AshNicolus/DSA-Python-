# #Brute Force
# def search(arr,k):
#     n = len(arr)
#     if n == 0 :
#         return [-1,-1]

    
#     low = 0
#     high = n - 1
#     while low <=high:
#         mid = (high+low)//2
#         if (arr[mid]==k ):
#             if (arr[mid-1] == arr[mid]):
#                 return [mid-1,mid]
#             elif (arr[mid] == arr[mid+1]):
#                 return [mid,mid+1]
#         elif(arr[mid]<k):
#             low = mid + 1
#         else:
#             high = mid - 1
#     return [-1,-1]

# # optimised code


from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target):
            low, high = 0, len(nums) - 1
            first = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    first = mid
                    high = mid - 1  # keep searching on the left side
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return first

        def findLast(nums, target):
            low, high = 0, len(nums) - 1
            last = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    last = mid
                    low = mid + 1  # keep searching on the right side
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return last
        
        first = findFirst(nums, target)
        if first == -1:
            return [-1, -1]
        
        last = findLast(nums, target)
        return [first, last]

