'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
'''

def longestPalindrome(s):
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer

    def helper(s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]
    res = ""
    for i in range(len(s)):
        # odd case, like "aba"
        tmp = helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = helper(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res

print(longestPalindrome(s="babad"))