'''
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.
'''

def removeDuplicates(S):
  """
  :type S: str
  :rtype: str
  """
  if not S: return ""
  # stack for check
  stk = []
  stk.append(S[0])

  for s in S[1:]:
    # if empty or not equal, append
    if not stk or s != stk[-1]:
      stk.append(s)
    # pop item if equal
    else:
      stk.pop()
    
  return "".join(stk)

print(removeDuplicates("abbaca"))
print(removeDuplicates("aaaaaaaa"))