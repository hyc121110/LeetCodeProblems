'''
Given an array, rotate the array to the right by k steps, where k is non-negative.
'''

# reverse the first n - k elements -> [4,3,2,1,5,6,7]
# reverse the rest of them -> [4,3,2,1,7,6,5]
# reverse the entire array -> [5,6,7,1,2,3,4]

def rotateArray(nums, k):
  # basic check
  if not k or k <= 0:
    return
  
  # number of rotationssi just k % len(nums)
  k, end = k % len(nums), len(nums) - 1
  reverse(nums, 0, end - k)
  reverse(nums, end - k + 1, end)
  reverse(nums, 0, end)

def reverse(nums, start, end):
  while start < end:
    nums[start], nums[end] = nums[end], nums[start]
    start += 1
    end -= 1

nums=[1,2,3,4,5,6,7]
rotateArray(nums, k=3)
print(nums)