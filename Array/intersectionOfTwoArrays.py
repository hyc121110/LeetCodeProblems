'''
Given two arrays, write a function to compute their intersection.
'''

def intersect(self, nums1, nums2):
  """
  :type nums1: List[int]
  :type nums2: List[int]
  :rtype: List[int]
  """
  counts = {}
  res = []

  # store count of elements in nums1
  for num in nums1:
      counts[num] = counts.get(num, 0) + 1

  # if element in nums2 is in nums1, append that element and reduce count
  for num in nums2:
      if num in counts and counts[num] > 0:
          res.append(num)
          counts[num] -= 1

  return res