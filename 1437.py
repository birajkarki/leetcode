# 1437. Check If All 1's Are at Least Length K Places Away
class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        spaces = k  
        for n in nums:
            if n == 1:
                if spaces < k:
                    return False
                spaces = 0  
            else:
                spaces += 1  

        return True


# -------------------------
# TEST CASES
# -------------------------

obj = Solution()

print("Test 1:", obj.kLengthApart([1,0,0,1,0,1], 2))  # False
print("Test 2:", obj.kLengthApart([1,0,0,0,1], 3))    # True
print("Test 3:", obj.kLengthApart([1,1,1], 0))        # True
print("Test 4:", obj.kLengthApart([1,1], 1))          # False
print("Test 5:", obj.kLengthApart([0,0,0], 2))        # True
print("Test 6:", obj.kLengthApart([], 2))             # True
print("Test 7:", obj.kLengthApart([1], 5))            # True
