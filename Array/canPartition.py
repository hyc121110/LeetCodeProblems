'''
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
'''

def canParititon(nums):
  # continue if sum of nums is even
  if sum(nums) & 1 == 0:
    # shift one bit to the right to find the sum of partition array
    target = sum(nums) >> 1
    # initialize set to 0
    cur = {0}
    for i in nums:
      # perform union operation (|) with rhs to add i + x to the set
      cur |= {i + x for x in cur}
      if target in cur:
        return True
  return False

print(canParititon(nums=[1,5,11,5]))
print(canParititon(nums=[1,2,3,4,5,6,7]))
print(canParititon(nums=[1,1]))