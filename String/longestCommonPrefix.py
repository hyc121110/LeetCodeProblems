'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

def longestCommonPrefix(strs):
    if not strs:
        return ""
    # find the shortest string as longer string
    # as longer string cannot be prefix
    strs = sorted(strs, key=len)
    shortest = strs[0]
    # idx for tracking current char that is common
    for idx, ch in enumerate(shortest):
        for other in strs[1:]:
            if other[idx] != ch:
                return shortest[:idx]
    return shortest 
    
print(longestCommonPrefix(strs=["flower","flow","flight"]))