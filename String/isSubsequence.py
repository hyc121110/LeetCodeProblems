'''
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.
'''

def isSubsequence(s, t):
  # iterate through one of the strings
  for c in s:
    # find char in the other strings (returns the index if found else -1)
    i = t.find(c)
    if i == -1: # not found
      return False
    else:
      # start searching the string after the character found
      t = t[i+1:]
  return True

print(isSubsequence(s = "abc", t = "ahbgdc"))
print(isSubsequence(s = "axc", t = "ahbgdc"))