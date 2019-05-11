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