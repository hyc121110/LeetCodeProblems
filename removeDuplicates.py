# Leetcode 

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