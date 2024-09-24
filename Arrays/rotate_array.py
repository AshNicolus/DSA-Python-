class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr(self, arr, k):
        # Handle cases where k > length of array
        k = k % len(arr)
        
        # Step 1: Reverse the first k elements
        self.reversarr(arr, 0, k-1)
        
        # Step 2: Reverse the rest of the array
        self.reversarr(arr, k, len(arr)-1)
        
        # Step 3: Reverse the entire array
        self.reversarr(arr, 0, len(arr)-1)
        
        return arr

    # Helper function to reverse elements in array from 'start' to 'end'
    def reversarr(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

# Test the function
arr = [1, 2, 3, 4, 5]
d = 2

solution = Solution()
rotated_arr = solution.rotateArr(arr, d)
print(rotated_arr)
