class Solution:
    def findTwoElement( self,arr): 
        # code here
        n= len(arr)
        S = (n*(n+1))/2
        P = (n*(n+1)*(2*n+1))/6
        
        S_actual = sum(arr)
        P_actual = sum(x*x for x in arr)
        
        diff_sum = S_actual - S
        diff_squares = P_actual - P
        sum_x_y = diff_squares//diff_sum
        
        x = int((diff_sum + sum_x_y)//2)
        y = int(sum_x_y - x)
        
        return [x,y]
        
        

