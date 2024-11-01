from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modify nums to its next lexicographical permutation in-place.
        """
        
        n = len(nums)
        
        # Step 1: Find the break point:
        ind = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind = i
                break
        
        # If no break point is found, the list is in descending order:
        if ind == -1:
            nums.reverse()
            return
        
        # Step 2: Find the next greater element to swap with nums[ind]:
        for i in range(n - 1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break
        
        # Step 3: Reverse the right half after the break point:
        nums[ind + 1:] = reversed(nums[ind + 1:])
