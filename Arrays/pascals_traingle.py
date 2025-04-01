class Solution:
    def ncr(self,n,r):
        def factorial(n):
            if n == 0 or n == 1:
                return 1
            return n * factorial(n-1)
        return factorial(n)//(factorial(n-r)*factorial(r))
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            temp = []
            for j in range(i+1):
                temp.append(self.ncr(i,j))
            ans.append(temp)
        return ans