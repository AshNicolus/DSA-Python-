class Solution:
    def findKRotation(self, arr):
        n = len(arr)
        low, high = 0, n - 1

        while low < high:
            mid = (low + high) // 2
            
            if arr[mid] < arr[high]:
                high = mid  
            else:
                low = mid + 1  

        return low  