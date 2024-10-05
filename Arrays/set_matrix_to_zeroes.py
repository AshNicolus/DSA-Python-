from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Modify the matrix in-place such that if an element is 0, 
        its entire row and column are set to 0.
        """
        n = len(matrix)    # Number of rows
        m = len(matrix[0])  # Number of columns
        col0 = 1  # This flag is used to mark if the first column should be zeroed
        
        # First pass: mark zeros in the first row and column
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # Mark the row
                    if j != 0:
                        matrix[0][j] = 0  # Mark the column
                    else:
                        col0 = 0  # Mark the first column to be zeroed
        
        # Second pass: use marks to set other elements to zero
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Set the first row to zero if needed
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0
        
        # Set the first column to zero if needed
        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0
