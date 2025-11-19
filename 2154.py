# 2154. Keep Multiplying Found Values by Two
class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        num_set = set(nums)
        while original in num_set:
            original *= 2
        return original


# -------------------------
# TEST CASES
# -------------------------
obj = Solution()
print("Test 1:", obj.findFinalValue([5,3,6,1,12], 3))  # 24
print("Test 2:", obj.findFinalValue([2,7,9], 4))        # 4
print("Test 3:", obj.findFinalValue([1,2,4,8,16], 1))  # 32
print("Test 4:", obj.findFinalValue([], 10))            # 10
print("Test 5:", obj.findFinalValue([10,20,40], 10))    # 80
