'''
Given an array nums of n integers where n > 1,  return an 
array output such that output[i] is equal to the product of
all the elements of nums except nums[i].

Solve it without division and O(n)
'''

def productExceptSelf(nums):
    p = 1
    n = len(nums)
    output = []
    for i in range(n):
        output.append(p)
        p = p * nums[i]
    p = 1
    for i in range(n-1,-1,-1):
        output[i] = output[i] * p
        p = p * nums[i]
    return output
    
print(productExceptSelf(nums=[1,2,3,4]))