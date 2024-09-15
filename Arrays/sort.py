# sort  for 0s , 1s and 2s 
class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        c0 = 0
        c1 = 0
        c2 = 0
        
        n = len(arr)
        
        for i in range(n):
            if arr[i] == 0 :
                c0 +=1
            elif arr[i] == 1:
                c1 +=1
            elif arr[i] == 2:
                c2 +=1
            
        i = 0 
        while(c0>0):
            arr[i] = 0
            i+= 1
            c0 -= 1
        
        while(c1>0):
            arr[i] = 1
            i += 1
            c1 -= 1
            
        while(c2>0):
            arr[i]  = 2
            i += 1
            c2 -= 1
            
        return arr
        