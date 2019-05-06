'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
'''

def canJump(self, nums: List[int]) -> bool:
    step = 0
    for i, n in enumerate(nums):
        if i > step:
            return False
        m = max(step, i+n)
    return True
    
print(canJump(nums=[2,3,1,1,4]))