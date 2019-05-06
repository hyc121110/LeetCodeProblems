'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
-The same word in the dictionary may be reused multiple times in the segmentation.
-You may assume the dictionary does not contain duplicate words.
'''

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