'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
'''

def maxProduct(nums):
  # initialize max product
  r = nums[0]

  # imax/imin stores the max/min product of subarray that ends with the current number A[i]
  imax = imin = r

  for num in nums[1:]:
    # multiplied by a negative makes big number smaller, small number bigger so we redefine the extremums by swapping them
    if num < 0:
      imax, imin = imin, imax
    
    # max/min product for the current number is either the current number itself or the max/min by the previous number times the current one
    imax = max(num, imax * num)
    imin = min(num, imin * num)

    r = max(r, imax)
  
  # the newly computed max value is a candidate for our global result
  return r

print(maxProduct(nums=[-2,0,-1]))