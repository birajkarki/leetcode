class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        # Length of the string
        n = len(s)
        
        # We will store:
        # left[x]  = first index where character x appears
        # right[x] = last index where character x appears
        #
        # There are 26 lowercase letters, so arrays of size 26.
        # Initialize to -1 meaning "not found yet".
        left = [-1] * 26
        right = [-1] * 26
        
        
        # ---------------------------------------------------------
        # Step 1: Find the FIRST and LAST occurrence of each letter
        # ---------------------------------------------------------
        #
        # Enumerate gives i = index, ch = character.
        # Convert character to number (0 to 25) using:
        #   ord(ch) - ord('a')
        #
        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')   # map 'a' → 0, 'b' → 1, ... 'z' → 25
            
            # If this is the first time we see this character,
            # record it in left[].
            if left[c] == -1:
                left[c] = i
            
            # Always update right[c] because the last occurrence
            # keeps changing as we scan the string.
            right[c] = i
        
        
        # ---------------------------------------------------------
        # Step 2: For each letter, check if it can be the outer
        #         characters of a 3-length palindrome.
        #
        # A palindrome of length 3 looks like:  X _ X
        #
        # So the same character must appear at least twice:
        #   left[c] < right[c]
        #
        # The middle character can be anything.
        # Count how many UNIQUE characters appear between them.
        # ---------------------------------------------------------
        
        ans = 0
        
        for c in range(26):    # Loop through each letter a–z (0 to 25)
            
            # Ignore if the character does not appear twice
            if left[c] != -1 and right[c] != -1 and left[c] < right[c]:
                
                # Extract the substring between first and last occurrence
                # Example: s = "aabca"
                # for 'a': left = 0, right = 4
                # middle substring = s[1 : 4] = "abc"
                #
                # We convert it to a set to get UNIQUE characters only.
                mids = set(s[left[c] + 1 : right[c]])
                
                # The number of unique middle characters equals
                # the number of unique palindromic subsequences of form "X Y X"
                ans += len(mids)
        
        # Return the final answer
        return ans


# -------------------------
# TEST CASES
# -------------------------

obj = Solution()
print("Test 1:", obj.countPalindromicSubsequence("aabca"))  # Expected: 3
print("Test 2:", obj.countPalindromicSubsequence("adc"))    # Expected: 0
print("Test 3:", obj.countPalindromicSubsequence("bbcbaba"))  # Expected: 4
print("Test 4:", obj.countPalindromicSubsequence("aaaaa"))  # Expected: 1
print("Test 5:", obj.countPalindromicSubsequence("abcabcabc"))  # Expected: 9