from typing import List

class Solution:
    def majorityElement(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        
        # Step 1: Find potential candidates
        candidate1, candidate2, count1, count2 = None, None, 0, 0
        
        for num in arr:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Step 2: Verify candidates
        result = []
        for candidate in [candidate1, candidate2]:
            if arr.count(candidate) > len(arr) // 3:
                result.append(candidate)
        
        return result
