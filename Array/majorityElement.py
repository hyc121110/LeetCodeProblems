'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''

from collections import defaultdict

def majorityElement(nums):
  # method 1
  d = defaultdict(int)

  for num in nums:
    d[num] += 1

  max_val = max(list(d.values()))

  for key, val in d.items(): # iterate through the dict
    if val == max_val:
      return key

  # method 2: NOTICE that the majority element always exist in the array,so that the middle always is the answer
  # return sorted(num)[len(num)/2]

print(majorityElement(nums=[2,2,1,1,1,2,2]))