'''
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.
'''

def gcdOfStrings(str1, str2):
  if len(str1) == len(str2):
    return str1 if str1==str2 else ''
  else:
    if len(str1) < len(str2):
      # swap
      str1, str2 = str2, str1
    # check if the shorter string has common pattern
    if str1[:len(str2)] == str2:
      # shorten str1 and check with str2 until the same
      return gcdOfStrings(str1[len(str2):], str2)
    else:
      return ''

str1 = "ABCABC"
str2 = "ABC"

print(gcdOfStrings(str1, str2))