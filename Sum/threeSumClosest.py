'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
'''

def threeSumClosest(nums, target):
    nums.sort()
    result = nums[0]+nums[1]+nums[2]
    for i in range(len(nums)-2):
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i]+nums[l]+nums[r]
            if s == target:
                # found
                return s
            # compare difference between new diff and old diff
            # if new < old, update old
            if abs(s-target) < abs(result-target):
                result = s
            # shift indices based on diff between result and target
            if s < target:
                l += 1
            elif s > target:
                r -= 1
    return result

print(threeSumClosest(nums=[-1, 2, 1, -4], target = 1))