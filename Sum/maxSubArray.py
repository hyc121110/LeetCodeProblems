'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
'''

def maxSubArray(nums):
    # initialize max sum
    max_sum = nums[0]
    for i in range(1,len(nums)):
        if nums[i] + nums[i-1] > nums[i]:
            # replaced nums[i] with the sum of nums[i] and nums[i-1]
            nums[i] = nums[i] + nums[i-1]
        # update max_sum if 
        if nums[i] > max_sum:
            max_sum = nums[i]
    return max_sum

print(maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray(nums=[-2,1]))