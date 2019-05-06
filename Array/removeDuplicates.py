'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''

def removeDuplicates(nums):
    if not nums:
        return 0
    
    new_tail = 0
    
    for i in range(1, len(nums)):
        if nums[i] != nums[new_tail]:
            new_tail += 1
            nums[new_tail] = nums[i]
            
    return new_tail+1
    
print(removeDuplicates(nums=[0,0,1,1,1,2,2,3,3,4]))