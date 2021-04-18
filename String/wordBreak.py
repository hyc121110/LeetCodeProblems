'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
-The same word in the dictionary may be reused multiple times in the segmentation.
-You may assume the dictionary does not contain duplicate words.
'''

"""
The idea is the following:

d is an array that contains booleans

d[i] is True if there is a word in the dictionary that ends at ith index of s AND d is also True at the beginning of the word

Example:

s = "leetcode"

words = ["leet", "code"]

d[3] is True because there is "leet" in the dictionary that ends at 3rd index of "leetcode"

d[7] is True because there is "code" in the dictionary that ends at the 7th index of "leetcode" AND d[3] is True

The result is the last index of d.
"""
def wordBreak(s, wordDict):
    d = [False] * len(s)
    for i in range(len(s)):
        for w in wordDict:
            l = i-len(w)
            r = i+1
            if w == s[l+1:r] and (d[l] or l == -1):
                d[i] = True
    return d[-1]
    
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(wordBreak(s, wordDict))

# adding one element for better optimization
def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
    dp = [False] * (len(s)+1)
    dp[0] = True
    
    for i in range(1,len(s)+1):
        for word in wordDict:
            l = i - len(word)
            r = i
            
            if word == s[l:r] and dp[l]:
                dp[i] = True
                break
                
    return dp[-1]