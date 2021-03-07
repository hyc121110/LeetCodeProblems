"""
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.
"""

class Solution:
    def minDeletions(self, s: str) -> int:
        # dict to count frequency
        d = {}
        
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
                
        # counter to keep track how many characters needs to be deleted
        res = 0
        # set to store unique frequencies
        _set = set()
        
        for val in d.values():
            # decrement freq until the set doesn't have the freq
            while val in _set and val > 0:
                val -= 1
                res += 1
            _set.add(val)
            
        return res

# time complexity: O(n^2) as need to iterate the string once and the while loop's time depends on frequency of characters in string
# space complexity: O(n+m), using dictionary and set to keep track

# 2nd solution: using collections.Counter
from collections import Counter
class Solution2:
    def minDeletions(self, s: str) -> int:
        cnt, res, used = Counter(s), 0, set()
        for _, freq in cnt.items():
            while freq > 0 and freq in used:
                freq -= 1
                res += 1
            used.add(freq)
        return res