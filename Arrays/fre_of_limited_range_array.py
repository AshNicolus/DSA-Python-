# Method 1 :
class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # Step 1: Replace elements greater than N with 0
        for i in range(N):
            if arr[i] > N:
                arr[i] = 0
        
        # Step 2: Use the array to count the frequency
        # We use (N+1) as a multiplier to store both original values and counts.
        for i in range(N):
            # (arr[i] % (N+1)) gives us the original value (between 1 and N).
            if arr[i] % (N+1) > 0:
                # Update the count at the index corresponding to the value (arr[i] % (N+1)) - 1
                arr[(arr[i] % (N+1)) - 1] += (N+1)
        
        # Step 3: Final pass to get the counts
        for i in range(N):
            # Divide by (N+1) to get the actual frequency of each number
            arr[i] //= (N+1)


# Method 2 using hash / dict :

class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # Step 1: Initialize a dictionary to store the frequency of elements.
        freq = {}
        
        # Step 2: Count the frequency of each element in the array, but only for elements between 1 and N.
        for num in arr:
            if 1 <= num <= N:
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1
        
        # Step 3: Update the original array with the frequency of each number from 1 to N.
        for i in range(N):
            arr[i] = freq.get(i + 1, 0)

