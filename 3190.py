# 3190. Minimum Operations to Make All Array Elements Divisible by 3


from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0

        for n in nums:
            remainder = n % 3   # find remainder when dividing by 3
            
            if remainder == 1:
                # Example: 4,7,10…
                # Only need to subtract 1
                operations += 1
            
            elif remainder == 2:
                # Example: 2,5,8…
                # Only need to add 1
                operations += 1

            # remainder == 0 means divisible → no operation needed
        
        return operations

# -------------------------
# TEST CASES
# -------------------------

obj = Solution()
print("Test 1:", obj.minimumOperations([1,2,3,4,5,6]))  # Expected: 5
print("Test 2:", obj.minimumOperations([3,6,9]))        # Expected: 0
print("Test 3:", obj.minimumOperations([2,4,7,10]))  # Expected: 4
print("Test 4:", obj.minimumOperations([0,1,2]))        # Expected: 2
print("Test 5:", obj.minimumOperations([5,8,11,14]))  # Expected: 4