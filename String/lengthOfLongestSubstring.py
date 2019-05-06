def lengthOfLongestSubstring(s):
    # 2 pointers: pointer scan from left to right, pointer record first
    # character 
    if len(s) == 0: return 0
    # stores index of char's first occurence
    dict = {}
    
    start = max_length = 0
    for i in range(len(s)):
        if s[i] in dict and start <= dict[s[i]]:
            # if character in dict, update pointer
            # second check make sure don't enter just because we seen it before
            start = dict[s[i]] + 1
        else:
            # compare current max and new max
            max_length = max(max_length, i - start + 1)
        # update key's value
        dict[s[i]] = i
    
    return max_length

print(lengthOfLongestSubstring(s="dddggwetw"))