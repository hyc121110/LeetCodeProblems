'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

-The solution set must not contain duplicate triplets.
'''

def threeSum(nums):
    res = []
    nums.sort()
    for i in range(len(nums)-2):   
        # if not first element and numbers are the same -> skip
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # start from i+1 and last element of array
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1 
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                #increment l until the last duplicate
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                #decrement r until the first duplicate
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                #make sure the elem is different as we want unique solution
                l += 1; r -= 1
    return res

print(threeSum(nums=[-1, 0, 1, 2, -1, -4]))