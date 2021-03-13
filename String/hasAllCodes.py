"""
Given a binary string s and an integer k.

Return True if every binary code of length k is a substring of s. Otherwise, return False.
"""

# Time Complexity : O(N*k), where N is the size of string and k is length of binary code.
# Space Complexity : O(N*k)
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s)-k+1 < k: return False
        # set to track the binary substring
        _set = set()
        for i in range(len(s)-k+1):
            _set.add(s[i:i+k])
        
        return False if len(_set) < 2**k else True

# solution 2: going from backwards
# time complexity: O(n)
# space complexity: O(n)
class Solution2:
    def hasAllCodes(self, S: str, K: int) -> bool:
        count = 1 << K # same as 1 * 2^k
        seen = set()
        for i in range(len(S) - K, -1, -1):
            num = S[i:i+K]
            if num not in seen:
                seen.add(num)
                count -= 1
            if not count: return True # found all the required binaries
            if i < count: return False # there is no way to reach count with the remain i substrings