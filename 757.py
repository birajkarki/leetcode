# 757. Set Intersection Size At Least Two
from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Step 1⃣: Sort intervals by:
        #   1. end ascending  (x[1])
        #   2. start descending (-x[0])
        # This ordering ensures greedy choice works correctly.
        intervals.sort(key=lambda x: (x[1], -x[0]))

        # ans = total numbers we choose for the final containing set
        ans = 0

        # a and b are the last two chosen numbers in the global set
        # Initialize them to invalid values
        a, b = -1, -1

        # Step 2⃣: Process each interval
        for l, r in intervals:

            # Case 1️⃣: This interval has 0 selected numbers inside it
            # l > b means even the largest selected number 'b' is smaller than interval's start
            if l > b:
                # We must add TWO numbers to satisfy the interval
                # Greedy: pick r-1 and r (largest possible numbers)
                a = r - 1   # second last selected number
                b = r       # last selected number
                ans += 2
                # Continue to next interval
                continue

            # Case 2️⃣: Interval contains exactly 1 selected number
            # l <= b but l > a means:
            #   - b is inside the interval
            #   - a is NOT inside the interval
            elif l > a:
                # We must add ONE more number (r) to give interval 2 numbers
                a = b       # old 'b' becomes previous selected
                b = r       # new number added
                ans += 1
                continue

            # Case 3️⃣: Interval already has both 'a' and 'b'
            # l <= a < b <= r
            # So do nothing — interval is satisfied

        # Step 3⃣: Return minimum size of containing set
        return ans

# -------------------------
# TEST CASES
# -------------------------
obj = Solution()
print("Test 1:", obj.intersectionSizeTwo([[1,3],[1,4],[2,5],[3,5]]))  # 3
print("Test 2:", obj.intersectionSizeTwo([[1,2],[2,3],[2,4],[4,5]]))  # 5
print("Test 3:", obj.intersectionSizeTwo([[1,2],[2,3]]))              # 3
print("Test 4:", obj.intersectionSizeTwo([[1,5],[2,3],[4,5]]))          # 4
print("Test 5:", obj.intersectionSizeTwo([[1,10],[2,9],[3,8],[4,7]]))    # 2